def phi(x: int) -> int:
    if x == 1:
        return 0
    ret = x
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            while x % i == 0:
                x //= i
            ret -= ret // i
    if x > 1:
        ret -= ret // x
    return ret
for i in map(int, [*open(0)][:-1]):
    print(phi(i))
