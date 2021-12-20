n = int(input())
s = input()
count = 0
result = ''
for i in range(n):
    try:
        if s[i] + s[i + 1] + s[i + 2] == 'joi':
            count = 3
    except IndexError:
        pass
    if count:
        count -= 1
        result += s[i].upper()
    else:
        result += s[i]
print(result)
