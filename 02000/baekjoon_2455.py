people = 0; result = 0
for i in range(4):
    off, on = map(int, input().split())
    people += on - off
    result = max(result, people)
print(result)
