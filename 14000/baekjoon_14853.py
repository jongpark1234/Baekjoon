for _ in range(int(input())):
    n1, m1, n2, m2, p, result = *map(int, input().split()), 1, 0
    for i in range(m1 + 1):
        p *= (n1 - i + 1) / (n1 + n2 - i + 2)
    for i in range(1, m2 + 1):
        result += p
        p *= (m1 + i) / i * (n2 - i + 2) / (n1 + n2 - m1 - i + 2)
    print(result + p)
