people = 0
result = 0
for i in range(10):
    n, m = map(int, input().split())
    people += m - n
    result = max(result, people)
print(result)
