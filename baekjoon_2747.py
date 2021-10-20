n = int(input())
f1, f2 = 0, 1
for i in range(n - 1):
    f1, f2 = f1 + f2, f1
print(f1 + f2)
