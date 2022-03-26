from math import factorial
for _ in range(int(input())):
    n, m = map(int, input().split())
    print(factorial(m) // (factorial(n) * factorial(m - n)))
