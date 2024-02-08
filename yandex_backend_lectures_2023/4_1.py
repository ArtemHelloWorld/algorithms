def main():
    n = int(input())
    groups = sorted(list(map(int, input().split())))

    m = int(input())
    audiences = sorted(list(map(int, input().split())))

    res = 0
    current_group = groups[res]

    for audience in audiences:
        if audience >= current_group:
            res += 1
            if res >= n:
                print(n)
                return
            current_group = groups[res]
    print(res)


if __name__ == '__main__':
    main()