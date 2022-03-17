def ispalindrome(s):
    return s == s[::-1]
while True:
    s = input()
    if s == '#':
        break
    for i in range(len(s)):
        ds = s[:i] + s[i + 1:]
        if ispalindrome(ds):
            print(ds)
            break
    else:
        print('not possible')
