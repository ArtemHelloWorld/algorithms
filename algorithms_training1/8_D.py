def add(bin_tree, element):
    if element < bin_tree[0]:
        if bin_tree[1] is not None:
            add(bin_tree[1], element)
        else:
            bin_tree[1] = [element, None, None]
    elif element > bin_tree[0]:
        if bin_tree[2] is not None:
            add(bin_tree[2], element)
        else:
            bin_tree[2] = [element, None, None]
    else:
        return


def display(bin_tree):
    if bin_tree[1]:
        display(bin_tree[1])
    print(bin_tree[0])
    if bin_tree[2]:
        display(bin_tree[2])


def main():
    integers = list(map(int, input().split()))
    if len(integers) > 1:
        bin_tree = [integers[0], None, None]
        for integer in integers:
            if integer == 0:
                break
            add(bin_tree, integer)
        display(bin_tree)


if __name__ == '__main__':
    main()
