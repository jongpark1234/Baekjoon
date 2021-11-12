from sys import stdin
n = int(stdin.readline())
m = int(stdin.readline().rstrip())
s = stdin.readline().rstrip()
count = 0
result = 0
index = 1
while index < m - 1:
    if s[index - 1] == 'I' and s[index] == 'O' and s[index + 1] == 'I':
        count += 1
        if count == n:
            result += 1; count -= 1
        index += 1
    else:
        count = 0
    index += 1
print(result)
