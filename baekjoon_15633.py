n = int(input())
numlist = []
for i in range(1, n + 1):
    if n % i == 0:
        numlist.append(i)
print(sum(numlist) * 5 - 24)
