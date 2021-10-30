s = input()
palindrome = True
for i in range(int(len(s) / 2)):
    if s[i] != s[len(s) - 1 - i]:
        palindrome = False
print(str(palindrome).lower())
