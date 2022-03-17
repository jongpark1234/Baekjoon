from math import gcd
n = int(input())
a = list(map(int, input().split()))
x = int(input())
coprime = []
for i in a:
    if gcd(x, i) == 1:
        coprime.append(i)
print(sum(coprime) / len(coprime))
