a, b = 0, 1
for _ in range(int(input())):
    a, b = (a + b) % 1000000007, a % 1000000007
print(a)
