MAX = 7500000
prime = [True for _ in range(MAX)]
for i in range(2, int(MAX ** 0.5) + 1):
    if prime[i]:
        for j in range(i * 2, MAX, i):
            prime[j] = False
prime = [i for i in range(2, MAX) if prime[i]]
k = int(input())
print(prime[k - 1])
