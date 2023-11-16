s = input()
for i in range(len(s)):
    if i == 0:
        temp = s[i]
    else:
        if s[i] != temp:
            print(i)
            break
else:
    print(i + 1)
