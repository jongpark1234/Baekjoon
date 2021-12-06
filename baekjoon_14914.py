a, b = map(int, input().split())
mineral = []
for i in range(1, a + 1):
    if not b % i and not b % i:
        mineral.append(i)
for i in mineral:
    if i * (a // i) == a and i * (b // i) == b:
        print(i, a // i, b // i)
