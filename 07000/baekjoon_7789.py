def isprime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
phone, n = input().split()
print('Yes' if all(map(isprime, map(int, [phone, n + phone]))) else 'No')
