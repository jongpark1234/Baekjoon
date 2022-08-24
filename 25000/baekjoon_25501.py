def recursion(l, r):
    global result
    result += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(l + 1, r - 1)
for _ in range(int(input())):
    s, result = input(), 0
    recursion(0, len(s) - 1)
    print(+(s == s[::-1]), result)
