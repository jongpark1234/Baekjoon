m, n = map(int, input().split())
def isprime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if not num % i:
                return False
        return True
for i in range(m, n + 1):
    if isprime(i):
        print(i)
