def calc(x):
    return sum((x + 1 >> i + 1 << i) + max(0, (x + 1) % (1 << i + 1) - (1 << i)) for i in range(55))
a, b = map(int, input().split())
print(calc(b) - calc(a - 1))
