def add(bin_tree, element):
    if bin_tree[0] < element:
        if bin_tree[1] is not None:
            add(bin_tree[1], element)
        else:
            bin_tree[1] = [element, None, None]
    elif bin_tree[0] > element:
        if bin_tree[2] is not None:
            add(bin_tree[2], element)
        else:
            bin_tree[2] = [element, None, None]
    else:
        return


def find_height(bin_tree, height=1):
    maxx = height
    if bin_tree[1] is not None:
        maxx = max(find_height(bin_tree[1], height + 1), maxx)

    if bin_tree[2] is not None:
        maxx = max(find_height(bin_tree[2], height + 1), maxx)

    return maxx


def main():
    integers = list(map(int, input().split()))
    if len(integers) > 1:
        bin_tree = [integers[0], None, None]
        for integer in integers:
            if integer == 0:
                break
            add(bin_tree, integer)

        print(find_height(bin_tree))
    else:
        print(0)


if __name__ == '__main__':
    main()
