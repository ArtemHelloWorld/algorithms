

def calculate(string):
    counter = {
        's': 0,
        'h': 0,
        'e': 0,
        'r': 0,
        'i': 0,
        'f': 0,
    }

    for s in string:
        if s in 'sherif':
            counter[s] += 1

    counter['f'] = counter['f'] // 2

    return min(list(counter.values()))

def main():
    string = input()
    print(calculate(string))


if __name__ == '__main__':
    main()


