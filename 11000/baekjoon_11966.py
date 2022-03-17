n = int(input())
for i in range(31):
    if 2 ** i == n:
        print(1)
        exit(0)
    elif 2 ** i > n:
        break
print(0)
