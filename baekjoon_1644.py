sieve = [True for _ in range(4000001)]
for i in range(2, int(4000001 ** 0.5)):
    if sieve[i]:
        for j in range(i + i, 4000001, i):
            sieve[j] = False
primes = [i for i, j in enumerate(sieve) if j and i >= 2]
sumlist = [0] * (len(primes) + 1)
for i in range(len(primes)):
    sumlist[i + 1] = sumlist[i] + primes[i]
n = int(input())
result = 0
left, right = 0, 1
while left < len(primes) and primes[right - 1] <= n:
    if sumlist[right] - sumlist[left] == n:
        result += 1
        left += 1
    elif sumlist[right] - sumlist[left] > n:
        left += 1
    else:
        if right < len(sumlist) - 1:
            right += 1
        else:
            left += 1
print(result)
