import base64
import collections
import sys
from binascii import unhexlify
from typing import Optional, Union

import requests


class SmartHub:
    def __init__(self, url, address):
        self.url = url
        self.address = address
        self.serial = 1
        self.dev_type = 1
        self.dev_name = 'HUB01'

        self.decoder = Decoder()
        self.encoder = Encoder()

        self.devices = []
        self.timestamp = None
        self.timestamp_whoishere = None

    def start_hub(self):
        self.who_is_here()
        self.handle_new_packets()

    def handle_new_packets(self):
        while True:
            self.get_all_statuses()
            print(self.devices)
            print()

    def who_is_here(self):
        payload = {
            'src': self.address,
            'dst': 16383,
            'serial': self.serial,
            'dev_type': self.dev_type,
            'cmd': 1,
            'cmd_body': {
                'dev_name': self.dev_name
            }
        }
        response = self.send_data(payload)
        self.devices = []
        self._process_response(response)

    def i_am_here(self):
        payload = {
            'src': self.address,
            'dst': 16383,
            'serial': self.serial,
            'dev_type': self.dev_type,
            'cmd': 2,
            'cmd_body': {
                'dev_name': self.dev_name
            }
        }
        response = self.send_data(payload)
        self._process_response(response)

    def get_all_statuses(self):
        for device in self.devices:
            self.get_status(device)

    def get_status(self, device):
        if not device['broken'] and device['dev_type'] not in (6, ) and len(device['req_time']) < 10:

            payload = {
                'src': self.address,
                'dst': device['src'],
                'serial': self.serial,
                'dev_type': device['dev_type'],
                'cmd': 3,
            }
            try:
                response = self.send_data(payload)
                device['req_time'].append(self._read_timestamp(response))

                if response:
                    self._process_response(response)
            except Exception:
                return

    def set_status(self, device: dict, status: int):
        print(device['dev_type'], status)
        if not device['broken'] and device['dev_type'] not in (6, ) and len(device['req_time']) < 10:
            payload = {
                'src': self.address,
                'dst': device['src'],
                'serial': self.serial,
                'dev_type': device['dev_type'],
                'cmd': 5,
                'cmd_body': {
                    'value': status
                }
            }
            response = self.send_data(payload)
            device['req_time'].append(self._read_timestamp(response))

            self._process_response(response)

    def send_data(self, data: dict = None) -> list:
        if data:
            payload_encoded = self.encoder.encode_packet(data)
            response = requests.post(url=self.url, data=payload_encoded)
        else:
            response = requests.post(url=self.url)
        status_code = response.status_code

        if status_code == 200:
            self.serial += 1
            return self.decoder.decode_packets(response.text)

        elif status_code == 204:
            raise SystemExit(0)
        else:
            raise SystemExit(99)

    def _process_response(self, response: list):
        self._read_timestamp(response)

        for payload in response:
            # WHOISHERE or IAMHERE
            if payload['cmd'] == 1 or payload['cmd'] == 2:
                if payload['cmd'] == 1:
                    self.i_am_here()
                if payload['cmd'] == 2 and self.timestamp - self.timestamp_whoishere > 300:
                    continue

                # добавляем откликнувшееся устройство в список
                device = {
                    'src': payload['src'],
                    'dev_type': payload['dev_type'],
                    'dev_name': payload['cmd_body']['dev_name'],
                    'broken': False,
                    'req_time': collections.deque()
                }

                # EnvSensor
                if payload['dev_type'] == 2:
                    device['sensors'] = payload['cmd_body']['dev_props']['sensors']
                    device['triggers'] = payload['cmd_body']['dev_props']['triggers']

                # Switch
                elif payload['dev_type'] == 3:
                    device['dev_names'] = payload['cmd_body']['dev_props']['dev_names']

                self.devices.append(device)

            # STATUS
            elif payload['cmd'] == 4:
                for device in self.devices:
                    if device['src'] == payload['src']:
                        # EnvSensor
                        if payload['dev_type'] == 2:
                            values = collections.deque(payload['cmd_body']['values'])
                            values_arr = []
                            for sensor in str(device['sensors']):
                                if sensor == '0':
                                    values_arr.append(None)
                                else:
                                    values_arr.append(values.popleft())

                            for trigger in device['triggers']:
                                op = str(trigger['op'])
                                value = trigger['value']
                                name = trigger['name']
                                type_sensor = int(op[2:], 2)

                                if (op[1] == '0' and values_arr[type_sensor] < value) or (op[1] == '1' and values_arr[type_sensor] > value):
                                    for device1 in self.devices:
                                        if device1['dev_name'] == name:
                                            self.set_status(device1, int(op[0]))
                                            break

                        # Switch
                        elif payload['dev_type'] == 3:
                            value = payload['cmd_body']['value']
                            device.setdefault('req_time', collections.deque())
                            if self.timestamp - device['req_time'][0] <= 300:
                                device['req_time'].popleft()
                                for dependent_device_name in device['dev_names']:
                                    for dependent_device in self.devices:
                                        if dependent_device['dev_name'] == dependent_device_name:
                                            if 'active' not in dependent_device:
                                                self.get_status(dependent_device)
                                            if dependent_device.get('active') != value:
                                                self.set_status(dependent_device, value)
                                            break
                            else:
                                device['broken'] = True
                        elif payload['dev_type'] in (4, 5):
                            value = payload['cmd_body']['value']
                            device['active'] = value
                        break

    def _read_timestamp(self, response):
        for payload in response:
            if payload['cmd'] == 6:
                self.timestamp = payload['cmd_body']['timestamp']
                if not self.timestamp_whoishere:
                    self.timestamp_whoishere = self.timestamp
                return self.timestamp


class Decoder:
    """Класс для декодирования пакетов в JSON формат"""

    def decode_packets(self, packets: Optional[Union[bytes, str]]) -> list:
        if isinstance(packets, str):
            packets = packets.encode('utf-8')

        res = []
        packets = base64.urlsafe_b64decode(packets + b'=' * (-len(packets) % 4))
        while len(packets):
            length, payload = self.decode_packet(packets)
            res.append(self.pack_payload_in_json(payload))
            packets = packets[length + 2:]
        print(res)
        return res

    def decode_packet(self, packet: bytes) -> tuple:
        length = self._byte_to_int(packet[0])
        payload = self._bytes_to_int(packet[1:length + 1])
        crc8 = packet[length + 1]

        encoder = Encoder()
        if (crc8 != int(hex(encoder.int_to_crc8(packet[1:length + 1]))[2:], 16)) or (
                len(packet[1:length + 1]) != length):
            raise SystemExit(99)

        return length, payload

    @staticmethod
    def pack_payload_in_json(payload: list):
        if len(payload) < 5:
            raise SystemExit(99)

        res = {
            'src': payload[0],
            'dst': payload[1],
            'serial': payload[2],
            'dev_type': payload[3],
            'cmd': payload[4],
            'cmd_body': {}
        }

        # WHOISHERE or IAMHERE (одинаковые структуры)
        if res['cmd'] == 1 or res['cmd'] == 2:
            dev_name_length = payload[5]
            i = 6 + dev_name_length
            res['cmd_body']['dev_name'] = ''.join(list(map(chr, payload[6:i])))

            # EnvSensor
            if res['dev_type'] == 2:
                res['cmd_body']['dev_props'] = {}
                res['cmd_body']['dev_props']['sensors'] = ('0' * (4 - len(format(payload[i], 'b'))) + format(payload[i], 'b'))
                res['cmd_body']['dev_props']['triggers'] = []
                i += 1
                triggers_length = payload[i]
                for trigger in range(triggers_length):
                    op = '0' * (4 - len(format(payload[i+1], 'b'))) + format(payload[i+1], 'b')
                    value = payload[i + 2]
                    name_length = payload[i + 3]
                    name = ''.join(list(map(chr, payload[i + 4:i + 4 + name_length])))
                    res['cmd_body']['dev_props']['triggers'].append(
                        {
                            'op': op,
                            'value': value,
                            'name': name
                        }
                    )
                    i += name_length + 3

            # Switch
            elif res['dev_type'] == 3:
                res['cmd_body']['dev_props'] = {}
                res['cmd_body']['dev_props']['dev_names'] = []
                for _ in range(payload[i]):
                    i += 1
                    res['cmd_body']['dev_props']['dev_names'].append(
                        ''.join(list(map(chr, payload[i + 1:i + 1 + payload[i]]))))
                    i += payload[i]

        # GETSTATUS (отправляетсся только хабом)
        elif res['cmd'] == 3:
            return None

        # STATUS
        elif res['cmd'] == 4:
            # EnvSensor
            if res['dev_type'] == 2:
                values_length = payload[5]
                res['cmd_body']['Values'] = payload[6:6 + values_length]
            # Switch or Lamp or Socket
            elif res['dev_type'] in (3, 4, 5):
                res['cmd_body']['value'] = payload[5]

        # SETSTATUS (отправляетсся только хабом)
        elif res['cmd'] == 5:
            return None

        # TICK
        elif res['cmd'] == 6:
            res['cmd_body']['timestamp'] = payload[5]

        return res

    def _bytes_to_int(self, bytes_arr: bytes, index: int = 0) -> list:
        val = 0
        shift = 0
        while True:
            b = bytes_arr[index]
            val |= (b & 0x7f) << shift
            if (b & 0x80) == 0:
                break
            shift += 7
            index += 1

        if len(bytes_arr) > index + 1:
            return [val] + self._bytes_to_int(bytes_arr, index + 1)
        else:
            return [val]

    @staticmethod
    def _byte_to_int(byte) -> int:
        return byte & 0x7f


class Encoder:
    """Класс для кодирования JSON в пакет"""

    def encode_packet(self, packet: dict):
        cmd = packet['cmd']

        # WHOISHERE or IAMHERE
        if cmd == 1 or cmd == 2:
            return self.encode_WHOISHERE_IAMHERE(packet)
        # GETSTATUS
        elif cmd == 3:
            return self.encode_GETSTATUS(packet)
        # SETSTATUS
        elif cmd == 5:
            return self.encode_SETSTATUS(packet)

    def encode_WHOISHERE_IAMHERE(self, data: dict):
        payload = (
                self.int_to_leb128(data['src']) +
                self.int_to_leb128(data['dst']) +
                self.int_to_leb128(data['serial']) +
                self.int_to_leb128(data['dev_type']) +
                self.int_to_leb128(data['cmd']) +
                len(data['cmd_body']['dev_name']).to_bytes(1, "big") +
                data['cmd_body']['dev_name'].encode('utf-8')
        )
        return self.wrap_payload_in_packet(payload)

    def encode_GETSTATUS(self, data: dict):
        payload = (
                self.int_to_leb128(data['src']) +
                self.int_to_leb128(data['dst']) +
                self.int_to_leb128(data['serial']) +
                self.int_to_leb128(data['dev_type']) +
                self.int_to_leb128(data['cmd'])
        )
        return self.wrap_payload_in_packet(payload)

    def encode_SETSTATUS(self, data: dict):
        payload = (
                self.int_to_leb128(data['src']) +
                self.int_to_leb128(data['dst']) +
                self.int_to_leb128(data['serial']) +
                self.int_to_leb128(data['dev_type']) +
                self.int_to_leb128(data['cmd']) +
                self.int_to_leb128(data['cmd_body']['value'])
        )
        return self.wrap_payload_in_packet(payload)

    def wrap_payload_in_packet(self, payload):
        length = len(payload)
        crc8 = hex(self.int_to_crc8(payload))[2:]
        packet = self.int_to_leb128(length) + payload + unhexlify('0' * bool(len(crc8) == 1) + crc8)
        return base64.urlsafe_b64encode(packet).decode('utf-8').rstrip('=')

    @staticmethod
    def int_to_leb128(i: int) -> bytearray:
        assert i >= 0
        r = []
        while True:
            byte = i & 0x7f
            i = i >> 7
            if i == 0:
                r.append(byte)
                return bytearray(r)
            r.append(0x80 | byte)

    def int_to_crc8(self, bytes_):
        CRC_TABLE = [
            0, 29, 58, 39, 116, 105, 78, 83, 232, 245, 210, 207, 156, 129, 166, 187,
            205, 208, 247, 234, 185, 164, 131, 158, 37, 56, 31, 2, 81, 76, 107, 118,
            135, 154, 189, 160, 243, 238, 201, 212, 111, 114, 85, 72, 27, 6, 33, 60,
            74, 87, 112, 109, 62, 35, 4, 25, 162, 191, 152, 133, 214, 203, 236, 241,
            19, 14, 41, 52, 103, 122, 93, 64, 251, 230, 193, 220, 143, 146, 181, 168,
            222, 195, 228, 249, 170, 183, 144, 141, 54, 43, 12, 17, 66, 95, 120, 101,
            148, 137, 174, 179, 224, 253, 218, 199, 124, 97, 70, 91, 8, 21, 50, 47,
            89, 68, 99, 126, 45, 48, 23, 10, 177, 172, 139, 150, 197, 216, 255, 226,
            38, 59, 28, 1, 82, 79, 104, 117, 206, 211, 244, 233, 186, 167, 128, 157,
            235, 246, 209, 204, 159, 130, 165, 184, 3, 30, 57, 36, 119, 106, 77, 80,
            161, 188, 155, 134, 213, 200, 239, 242, 73, 84, 115, 110, 61, 32, 7, 26,
            108, 113, 86, 75, 24, 5, 34, 63, 132, 153, 190, 163, 240, 237, 202, 215,
            53, 40, 15, 18, 65, 92, 123, 102, 221, 192, 231, 250, 169, 180, 147, 142,
            248, 229, 194, 223, 140, 145, 182, 171, 16, 13, 42, 55, 100, 121, 94, 67,
            178, 175, 136, 149, 198, 219, 252, 225, 90, 71, 96, 125, 46, 51, 20, 9,
            127, 98, 69, 88, 11, 22, 49, 44, 151, 138, 173, 176, 227, 254, 217, 196]
        crc = 0
        for b in bytes_:
            data = b ^ crc
            crc = CRC_TABLE[data]
        return crc


def get_config_data():
    if len(sys.argv) == 3:
        url = sys.argv[1]
        address = int(sys.argv[2], 16)
        return url, address
    raise SystemExit(0)


def main():
    url, address = get_config_data()

    smart_hub = SmartHub(url, address)
    smart_hub.start_hub()


if __name__ == '__main__':
    main()
