import sys
while True:
    palin = 'yes'
    s = sys.stdin.readline().rstrip()
    if s == '0':
        break
    for j in range(int(len(s) / 2)):
        if s[j] != s[-1 * (j + 1)]:
            palin = 'no'
            break
    print(palin)
