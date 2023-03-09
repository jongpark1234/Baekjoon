from sys import stdin
def ccw(a: list[int], b: list[int], c: list[int]) -> int:
    return (a[0] * b[1] + b[0] * c[1] + c[0] * a[1]) - (a[1] * b[0] + b[1] * c[0] + c[1] * a[0])
for _ in range(int(stdin.readline())):
    results, chList = [], []
    n, *numlist = map(int, stdin.readline().split())
    visited = [False for _ in range(n)]
    poslist = sorted([(numlist[i << 1], numlist[(i << 1) + 1], i) for i in range(n)])
    for i in range(n):
        while len(chList) >= 2 and ccw(chList[-2], chList[-1], poslist[i]) < 0:
            visited[chList.pop()[2]] = False
        chList.append(poslist[i])
        visited[poslist[i][2]] = True
    for i in poslist:
        if not visited[i[2]]:
            results.append(i[2])
    for i in chList[::-1]:
        results.append(i[2])
    print(*results)
