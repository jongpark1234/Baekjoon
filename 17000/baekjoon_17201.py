n = int(input())
s = input()
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        print('No')
        exit(0)
print('Yes')
