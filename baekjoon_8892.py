from itertools import combinations
from sys import stdin
def ispalindrome(x):
    if x == x[::-1]:
        return True
    return False
for i in range(int(stdin.readline())):
    words = list(combinations([stdin.readline().rstrip() for _ in range(int(stdin.readline()))], 2))
    result = '0'
    for i in words:
        if ispalindrome(i[0] + i[1]):
            result = i[0] + i[1]
            break
        elif ispalindrome(i[1] + i[0]):
            result = i[1] + i[0]
            break
    print(result)
