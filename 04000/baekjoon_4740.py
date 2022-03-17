while True:
    s = input()
    if s == '***':
        break
    for i in reversed(range(len(s))):
        print(s[i], end='')
    print()
