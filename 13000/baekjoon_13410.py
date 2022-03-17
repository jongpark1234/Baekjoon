n, k = map(int, input().split())
numlist = []
for i in range(1, k + 1):
    numlist.append(int(str(n * i)[::-1]))
print(max(numlist))
