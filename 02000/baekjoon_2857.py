from sys import stdin
result = ''
find = False
for i in range(5):
    if stdin.readline().rstrip().count('FBI'):
        find = True
        result += f'{i + 1} '
print(result if find else 'HE GOT AWAY!')
