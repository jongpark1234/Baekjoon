n = int(input())
numlist = list(map(int, input().split()))
count = 0
for i in numlist:
    if i == n:
        count += 1
print(count)