from sys import stdin
for _ in range(int(stdin.readline())):
    consist = True
    n = int(stdin.readline())
    tel = sorted([stdin.readline().strip() for _ in range(n)])
    for i in range(len(tel) - 1):
        if tel[i] == tel[i + 1][:len(tel[i])]:
            consist = False
            break
    print('YES' if consist else 'NO')
