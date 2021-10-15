def sub(x):
    global temp
    return x - temp
l, p = map(int, input().split())
numlist = list(map(int, input().split()))
temp = l * p
numlist = list(map(sub, numlist))
for i in numlist:
    print(i, end=" ")
