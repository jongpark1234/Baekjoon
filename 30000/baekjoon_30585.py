result = [0, 0]
h, w = map(int, input().split())
for i in range(h):
    s = input()
    for j in range(2):
        result[j] += .count(str(j))
print(min(result[0], result[1], h * w - result[0], h * w - result[1]))
