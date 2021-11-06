for _ in range(int(input())):
    s = input()
    print('Do-it' if s[len(s) // 2] == s[(len(s) // 2) - 1] else 'Do-it-Not')
