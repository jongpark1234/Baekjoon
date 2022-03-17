n, k = map(int, input().split())
member = [n for n in range(1, n + 1)]
jose = []
index = 0
for _ in range(n):
    for _ in range(k - 1):
        if index >= len(member) - 1:
            index = 0
        else:
            index += 1
    jose.append(member[index])
    del member[index]
    if index > len(member) - 1:
        index = 0
print("<", end='')
for i in jose:
    if i == jose[-1]:
        print(i, end = '')
    else:
        print("%s, " %(i), end='')
print(">")