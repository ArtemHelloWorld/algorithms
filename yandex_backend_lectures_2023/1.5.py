def read_data():
    with open('input.txt', 'r') as file:
        string = file.readline()
    return string


def write_data(answer: str) -> None:
    with open('output.txt', 'w') as file:
        file.write(answer)


def calculate(string: str) -> str:
    if len(string) == 1:
        return ''
    for i in range(len(string) // 2):
        if string[i] != 'a':
            ans = string[:i] + 'a' + string[i + 1:]
            return ans
    if string[:-1] == ' ':
        for i in range(1,len(string), -1):
            if string[:-i] != ' ':
                return string[:i] + 'b' + string[i + 1:]

    return string[:-1] + 'b'


def main():
    string = read_data()

    answer = calculate(string)
    write_data(f'{answer}')


if __name__ == '__main__':
    main()
