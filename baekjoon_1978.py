def isprime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
cnt = 0
n = int(input())
for i in map(int, input().split()):
    if isprime(i):
        cnt += 1
print(cnt)
