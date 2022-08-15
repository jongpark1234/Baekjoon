numlist = list(range(1, 21))
for _ in range(10):
    idx = 0
    a, b = map(int, input().split())
    a -= 1
    temp = numlist[a:b][::-1]
    for i in range(a, b):
        numlist[i] = temp[idx]
        idx += 1
print(*numlist)
