n = int(input())
string = list(input())
if n == 1:
    print('a')
    exit(0)
if n % 2 != 0:
    if string[n // 2] == '?':
        string[n // 2] = 'a'
for i in range(n // 2):
    if string[i] == string[-(i + 1)] == '?':
        string[i] = string[-(i + 1)] = 'a'
    elif string[i] == '?':
        string[i] = string[-(i + 1)]
    elif string[-(i + 1)] == '?':
        string[-(i + 1)] = string[i]
print(''.join(string))
