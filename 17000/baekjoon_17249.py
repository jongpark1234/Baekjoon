s = input()
count = [0, 0]
index = 0
for i in s:
    if i == '(':
        index += 1
    elif i == '@':
        count[index] += 1
print(*count)
