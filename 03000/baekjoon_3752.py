def D(n):
    result = 1
    if n == 1:
        return n
    for i in range(2, int(n ** 0.5) + 1):
        while not n % i:
            n //= i
            result *= i - 1 if n % i else i
    if n != 1:
        result *= n - 1
    return result
for _ in range(int(input())):
    determinant = 1
    input()
    for i in map(int, input().split()):
        determinant = determinant * D(i) % 1000000007
    print(determinant)
