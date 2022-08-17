result = 0
n = int(input())
for i in range(1, 101):
    for j in range(1, 101 - i):
        for k in range(1, 101 - i - j):
            if i >= j + 2 and j != 0 and k != 0 and k % 2 == 0 and i + j + k == n:
                result += 1
print(result)
