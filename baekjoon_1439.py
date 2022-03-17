s = input()
zero, one = 0, 0
for i in range(len(s)):
    if i == 0 or s[i - 1] != s[i]:
        if s[i] == '0':
            zero += 1
        else:
            one += 1
print(min(zero, one))
