from sys import stdin
for i in range(int(stdin.readline())):
    n = int(stdin.readline())
    print('YES' if str(n) == str(n ** 2)[-len(str(n)):] else 'NO')
