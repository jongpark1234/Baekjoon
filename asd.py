from math import log10
def get_index(r, c):
    n = max(abs(r), abs(c))
    return pow(n * 2 + 1, 2) - (
        n * 0 + n - c if r == n else
        n * 2 + n - r if c == -n else
        n * 4 + n + c if r == -n else
        n * 6 + n + r
    )
r1, c1, r2, c2 = map(int, input().split())
space = int(log10(get_index(r2, c2))) + 1
for i in range(r1, r2 + 1):
    for j in range(c1, c2 + 1):
        print(f'{get_index(j, -i):{" "}>{space}}', end=' ')
    print()
