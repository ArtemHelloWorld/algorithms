def main():
    N = int(input())
    numbers = list(map(int, input().split()))

    for ans in range(N):
        postfix = numbers[:ans][::-1]
        number_with_postfix = numbers + postfix
        if number_with_postfix == number_with_postfix[::-1]:
            print(ans)
            for i in postfix:
                print(i, end=' ')
            return


if __name__ == '__main__':
    main()
