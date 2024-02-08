def read_data():
    with open('input.txt', 'r') as file:
        n = int(file.readline())
        times = [x for x in file.readline().split()]
    return n, times


def write_data(answer: str) -> None:
    with open('output.txt', 'w') as file:
        file.write(answer)


def time_to_minutes(time: str) -> int:
    hours, minutes = time.split(':')

    return int(hours) * 60 + int(minutes)


def calculate(n, times) -> int:
    times = [time_to_minutes(time) for time in times]
    new_times = [time + 24 * 60 for time in times if time <= 720]

    times += new_times
    times.sort()

    minn = float('inf')
    for i in range(len(times)-1):
        diff = times[i+1] - times[i]
        if diff == 0:
            return diff
        minn = min(diff, minn)
    return minn


def main():
    n, times = read_data()

    min_range = calculate(n, times)

    write_data(f'{min_range}')


if __name__ == '__main__':
    main()
