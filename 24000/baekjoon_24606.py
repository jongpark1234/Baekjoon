n = int(input())
s = input()
for i in range(1, n):
    if s[i] == 'J':
        print(s[i - 1])
