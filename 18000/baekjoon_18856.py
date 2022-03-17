from sys import stdin
def isprime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if not num % i:
            return False
    return True
n = int(stdin.readline())
num = 2
cnt = 2
print(n)
print('1 2', end=' ')
for i in range(n - 3):
    num += 1
    print(num, end=' ')
while True:
    num += 1
    if isprime(num):
        print(num, end=' ')
        break
