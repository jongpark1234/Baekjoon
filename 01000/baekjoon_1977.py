m = int(input())
n = int(input())
sum = 0
numlist = []
for i in range(m, n + 1):
    if i ** 0.5 == int(i ** 0.5):
        sum += i
        numlist.append(i)
if len(numlist) == 0:
    print(-1)
else:
    print(sum, min(numlist), sep='\n')
