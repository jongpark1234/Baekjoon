n = int(input())
k = 64
while n % 2 == 0:
    n //= 2
    k -= 1
print(k)
