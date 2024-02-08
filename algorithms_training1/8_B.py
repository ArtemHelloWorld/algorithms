def add(bin_tree, element, height=1):
    height += 1
    if bin_tree[0] < element:
        if bin_tree[1] is not None:
            return add(bin_tree[1], element, height)
        else:
            bin_tree[1] = [element, None, None]
            return height
    elif bin_tree[0] > element:
        if bin_tree[2] is not None:
            return add(bin_tree[2], element, height)
        else:
            bin_tree[2] = [element, None, None]
            return height
    else:
        return None


def main():
    integers = list(map(int, input().split()))
    if len(integers) > 1:
        bin_tree = [integers[0], None, None]
        print(1, end=' ')
        for integer in integers:
            if integer == 0:
                break
            height = add(bin_tree, integer)
            if height is not None:
                print(height, end=' ')


if __name__ == '__main__':
    main()
