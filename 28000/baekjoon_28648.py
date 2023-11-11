result = float('inf')
for _ in range(int(input())):
    result = min(result, sum(map(int, input().split())))
print(result)
