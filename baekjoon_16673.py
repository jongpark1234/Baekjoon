wine = 0
c, k, p = map(int, input().split())
for n in range(1, c + 1):
    wine += (k * n) + (p * n ** 2)
print(wine)
