dots = 0
n = int(input())
for i in range(1, n + 1):
    for j in range(i + 1):
        dots += i + j
print(dots)
