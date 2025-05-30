def func(n):
    n_n = str(n)[::-1].lstrip('0')
    return int(n_n) if n_n != '' else '0'


a = []
for i in range(1, 1030):
    s = func(func(i))
    if s / i not in a:
        a.append((s / i))
print(a)