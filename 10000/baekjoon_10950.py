t = int(input())
numlist = []
for i in range(t):
    a, b = map(int, input().split())
    numlist.append(a + b)
for j in range(t):
    print(numlist[j])
