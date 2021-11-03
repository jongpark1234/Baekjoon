from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    wear = {}
    n = int(stdin.readline())
    if n == 0:
        print(0)
        continue
    for _ in range(n):
        wearname, weartype = map(str, stdin.readline().rstrip().split())
        if weartype in wear.keys():
            wear[weartype] += 1
        else:
            wear[weartype] = 1
        cases = 1
        for wearkey in wear.keys():
            cases *= wear[wearkey] + 1
    print(cases - 1)
