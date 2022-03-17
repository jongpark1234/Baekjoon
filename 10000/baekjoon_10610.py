from sys import stdin
n = sorted(list(stdin.readline().rstrip()), reverse=True)
sum = 0
if '0' not in n: print(-1)
else:
    for i in n: sum += int(i)
    print(''.join(n) if sum % 3 == 0 else -1)
