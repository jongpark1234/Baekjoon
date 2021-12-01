result = 0
s = input().split('-')
for i in s[0].split('+'):
    result += int(i)
for i in s[1:]:
    for j in i.split('+'):
        result -= int(j)
print(result)
