palin = True
s = input()
for i in range(int(len(s) / 2)):
    if s[i] != s[-1 * (i + 1)]:
        palin = False
        break
print(int(palin))
