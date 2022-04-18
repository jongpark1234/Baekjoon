def combination(a, b):
    result = 0
    value = b
    while a >= value:
        result += a // value
        value *= b
    return result
n, m = map(int, input().split())
print(min(combination(n, 5) - combination(m, 5) - combination(n - m, 5), combination(n, 2) - combination(m, 2) - combination(n - m, 2)))
