def main():
    pol = []
    otr = []

    numbers = list(map(int, input().split()))
    for number in numbers:
        if number > 0:
            pol.append(number)
            pol = sorted(pol)[max(-3, len(pol)*(-1)):]
        else:
            otr.append(number)
            otr = sorted(otr)[:min(3, len(otr))]

    if len(otr) == 3 and len(pol) == 3:
        if pol[0] * pol[1] * pol[2] >= otr[0] * otr[1] * otr[2]:
            print(pol[0], pol[1], pol[2])
        else:
            print(otr[0], otr[1], otr[2])
    # elif len(pol) == 3 and

if __name__ == '__main__':
    main()
