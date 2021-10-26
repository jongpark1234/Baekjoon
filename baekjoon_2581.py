import math
primes = []
m = int(input())
n = int(input())
for i in range(m, n + 1):
    prime = True
    if i > 1:
        for j in range(2, int(math.sqrt(i))):
            if i % j == 0:
                prime = not prime
                break
        if prime == True:
            primes.append(i)
if len(primes) == 0:
    print(-1)
else:
    print(sum(primes), min(primes), sep='\n')
