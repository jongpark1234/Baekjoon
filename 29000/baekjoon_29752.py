result = cur = 0
n = int(input())
for i in map(int, input().split()):
    cur = 0 if i == 0 else cur + 1
    result = max(result, cur)
print(result)
