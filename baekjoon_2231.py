n = int(input())
temp = 0
for i in range(n + 1):
    nlist = list(map(int, str(i)))
    if i + sum(nlist) == n:
        temp = i
        break
print(temp)
