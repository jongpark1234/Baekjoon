from sys import stdin
def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
while True:
    primes = [0]
    n = stdin.readline().rstrip()
    if n == '0':
        break
    for i in reversed(range(1, len(n) + 1)):
        for j in range(len(n) - i + 1):
            if isprime(int(n[j:i + j])) and int(n[j:i + j]) <= 100000:
                primes.append(int(n[j:i + j]))
    print(max(primes))
