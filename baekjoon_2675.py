t = int(input())
for i in range(t):
    r, s = input().split()
    r = int(r)
    for j in range(len(s)):
        print(s[j] * r, end="")
    print()
