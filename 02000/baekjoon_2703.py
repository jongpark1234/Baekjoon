from sys import stdin
for _ in range(int(input())):
    result = ''
    s = stdin.readline().rstrip()
    rule = stdin.readline().rstrip()
    for i in s:
        if i == ' ':
            result += ' '
        else:
            result += rule[ord(i) - 65]
    print(result)
