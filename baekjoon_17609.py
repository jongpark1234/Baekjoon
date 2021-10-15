from sys import *
def pseudoPalindrome(s, l, r):
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else: return 0
    return 1
def palindrome(s, l, r):
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            fs = pseudoPalindrome(s, l + 1, r)
            ss = pseudoPalindrome(s, l, r - 1)
            if (fs == 1) or (ss == 1): return 1
            else: return 2
    return 0

t = int(stdin.readline())
for i in range(t):
    string = list(stdin.readline().rstrip())
    print(palindrome(string, 0, len(string) - 1))
