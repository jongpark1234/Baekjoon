from sys import stdin
phi = [0 for _ in range(10001)]
def PHI(n):
    s = 1
    i = 2
    while i <= int(n ** 0.5):
        if n % i == 0:
            n //= i
            s *= i - 1
            while n % i == 0:
                s *= i
                n //= i
        i += 1 if i == 2 else 2
    return s * (1 if n - 1 == 0 else n - 1)
p = int(stdin.readline())
for i in range(2, 10001):
    phi[i] = phi[i - 1] + PHI(i) * 3
for i in range(1, p + 1):
    t, n = map(int, stdin.readline().split())
    if n == 1:
        print(f'{t} 1')
    else:
        print(f'{i} {phi[n] + 2}/2')
