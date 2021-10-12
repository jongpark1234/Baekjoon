n = int(input())
num = list(map(int, input()))
numlist = []
for i in range(n): numlist.append(num[i])
print(sum(numlist))