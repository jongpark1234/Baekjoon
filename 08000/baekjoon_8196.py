result = 0
n = int(input())
for i in sorted(map(int, input().split())):
    if i > result << 1:
        result = i - result
print(result)
