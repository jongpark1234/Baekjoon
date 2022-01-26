for _ in range(int(input())):
    s = input()
    temp = ''
    for i in range(10000):
        if len(s) <= i * i:
            m = i
            break
    s += '*' * (i * i - len(s))
    for i in range(m):
        for j in reversed(range(m)):
            char = s[m * j + i]
            if char != '*':
                temp += char
    print(temp)
