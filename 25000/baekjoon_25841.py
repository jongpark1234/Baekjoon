result = 0
a, b, d = map(int, input().split())
for i in range(a, b + 1):
    result += str(i).count(str(d))
print(result)
