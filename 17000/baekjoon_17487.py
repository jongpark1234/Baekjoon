cnt = 0
left = 'QWERTYASDFGGZXCVB'
count = [0, 0]
for i in input():
    if i.isupper():
        cnt += 1
    if i == ' ':
        cnt += 1
    else:
        count[i.upper() not in left] += 1
for i in range(cnt):
    count[count.index(min(count))] += 1
print(*count)
