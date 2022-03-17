from sys import stdin
for _ in range(int(stdin.readline())):
    numlist = sorted(list(map(int, stdin.readline().rstrip().split())))
    print(numlist[-3])
