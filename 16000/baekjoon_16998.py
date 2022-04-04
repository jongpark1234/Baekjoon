def F(a, b, c):
    if a + b > c:
        return 0
    if a < b:
        a, b = b, a
    return (((((a // b) * c + (a % b)) // a) - 1) // (a // b) * (2 * (((a // b) * c + (a % b)) // a) - (a // b) * (1 + ((((a // b) * c + (a % b)) // a) - 1) // (a // b))) // 2) + F(b, a % b, c - b * (((a // b) * c + (a % b)) // a))
for _ in range(int(input())):
    p, q, n = map(int, input().split())
    print(p * n * (n + 1) // 2 - q * ((p // q) * n * (n + 1) // 2 + F(p % q, q, p % q * (n + 1))))
