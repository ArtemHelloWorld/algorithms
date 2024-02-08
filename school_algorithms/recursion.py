import time
import matplotlib.pyplot as plt

r = 0
q = 0

def fn(n: int) -> int:
    s: int = 0
    for ii in range(0, 4*n):
        s = s * ii
    if n < 2:
        return s
    s = s + fn(n - 1)
    for j in range(0, 6):
        s = s + j * fn(n - 2)
    for k in range(0, 2 * n, 3):
        s += k
    return s
def f(n: int) -> int:
    global r, q
    if n >= 2:
        r += 1
        return 44 + 32 * n + f(n - 1) + 6 * f(n - 2)
    else:
        q += 1
        return 20 * n + 7


def formula(n):
    return 192/45 * 3 ** n - 247/45 * (-2) ** n - 5/3 * n + 74/9


def main():
    global r, q
    N_max = 30
    stats = []

    t1 = 0
    t2 = 0

    for N in range(0, N_max + 1):
        r = 0
        q = 0
        t1 = time.time()

        N_op = f(N)

        t2 = time.time()

        print(f'N = {N} r = {r} q = {q} r+q = {r + q} '
              f'N_op = {N_op} T = {round(t2 - t1, 2)}c')

        stats.append(formula(N)/(t2 - t1 + 0.0001))


    plt.plot(range(0, N_max+1)[0:], stats[0:])
    plt.title('C(N) = f(n) / T(n)')
    plt.show()

if __name__ == '__main__':
    main()
