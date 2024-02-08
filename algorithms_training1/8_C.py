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


def find_prev_maxx(bin_tree):
    prev = None
    curr = bin_tree[0]
    while bin_tree[2]:
        bin_tree = bin_tree[2]
        prev, curr = curr, bin_tree[0]
    if bin_tree[1]:
        bin_tree = bin_tree[1]
        while bin_tree[2]:
            bin_tree = bin_tree[2]
        return bin_tree[0]
    else:
        return prev


def main():
    integers = list(map(int, input().split()))
    if len(integers) > 1:
        bin_tree = [integers[0], None, None]
        for integer in integers:
            if integer == 0:
                break
            add(bin_tree, integer)
        print(find_prev_maxx(bin_tree))

if __name__ == '__main__':
    main()
