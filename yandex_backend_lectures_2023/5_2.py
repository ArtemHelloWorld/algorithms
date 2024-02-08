def check(counter: dict, k):
    print(counter)
    for v in counter.values():
        if 0 < v < k:
            return False
    return True


def main():
    n, k = tuple(map(int, input().split()))
    string = input()

    counter = {}
    for s in string:
        counter.setdefault(s, 0)
        counter[s] += 1

    left = 0
    right = n - 1

    while right - left + 1 >= k:
        if check(counter, k):
            return print(right - left + 1)

        if left == 0:
            while right != n - 1:
                counter[string[left]] -= 1
                counter[string[right + 1]] += 1

                left += 1
                right += 1
                if (
                        counter[string[right + 1]] == k and (counter[string[left]] >= k or counter[string[left]] == 0)
                ) or (
                        counter[string[right + 1]] > k and counter[string[left]] == 0
                ):
                    if check(counter, k):
                        return print(right - left + 1)

            counter[string[left]] -= 1
            left += 1

        elif right == n - 1:
            while left != 0:
                counter[string[left - 1]] += 1
                counter[string[right]] -= 1

                left -= 1
                right -= 1
                if (
                        counter[string[left - 1]] == k and (counter[string[right]] >= k or counter[string[right]] == 0)
                ) or (
                        counter[string[left - 1]] > k and counter[string[right]] == 0
                ):
                    if check(counter, k):
                        return print(right - left + 1)

            counter[string[right]] -= 1
            right -= 1
    print(0)


if __name__ == '__main__':
    main()
