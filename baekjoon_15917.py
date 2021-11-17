from sys import stdin
for i in range(int(stdin.readline())):
    a = int(stdin.readline())
    print(1 if (a & (-a)) == a else 0)
