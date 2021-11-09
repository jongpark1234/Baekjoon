from sys import stdin
count = 0
n = int(stdin.readline())
m = int(stdin.readline())
start = 0; end = n - 1
numlist = sorted(list(map(int, stdin.readline().split())))
while start < end:
    if numlist[start] + numlist[end] == m:
        count += 1
        start += 1
        end -= 1
    elif numlist[start] + numlist[end] < m:
        start += 1
    else:
        end -= 1
print(count)
