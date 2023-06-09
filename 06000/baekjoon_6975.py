from math import isqrt
def calc(n):
    properDivisors = []
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            properDivisors.append(i)
            if i ** 2 != n and i != 1:
                properDivisors.append(n // i)
    return sum(properDivisors)
for _ in range(int(input())):
    n = int(input())
    pd = calc(n)
    print(f'{n} is {"a deficient" if pd < n else "an abundant" if pd > n else "a perfect"} number.\n')
