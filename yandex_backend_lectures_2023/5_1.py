vasya = list(input())
petya = list(input())

v_dict = {}
p_dict = {}

for i, n in enumerate(vasya):
    v_dict.setdefault(n, set())
    v_dict[n].add(i)

for i, n in enumerate(petya):
    p_dict.setdefault(n, set())
    p_dict[n].add(i)

bik = 0
korov = 0

for k, v_val in v_dict.items():
    p_val = p_dict.get(k)
    if p_val:
        same = p_val & v_val

        bik += len(same)
        korov += min(len(v_val - same), len(p_val - same))

print(bik)
print(korov)
