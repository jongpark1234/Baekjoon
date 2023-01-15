for _ in range(int(input())):
    s = input()
    print(s[0], end='')
    for i in range(1, len(s)):
        print(s[i] if s[i] != s[i - 1] else '', end='')
    print()
