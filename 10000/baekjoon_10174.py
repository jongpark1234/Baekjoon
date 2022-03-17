n = int(input())
for i in range(n):
    palin = 'Yes'
    s = input().upper()
    for j in range(int(len(s) / 2)):
        if s[j] != s[-1 * (j + 1)]:
            palin = 'No'
            break
    print(palin)
