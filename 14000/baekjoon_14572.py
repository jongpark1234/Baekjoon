from sys import stdin
E = l = r = 0
n, k, d = map(int, stdin.readline().split())
studentList = sorted([[int(stdin.readline().split()[1]), list(map(int, stdin.readline().split()))] for _ in range(n)])
algorithmList = [0 for _ in range(k + 1)]
while l < n:
    any = all = 0
    while r < n and studentList[r][0] - studentList[l][0] <= d:
        for i in studentList[r][1]:
            algorithmList[i] += 1
        r += 1
    for i in range(1, k + 1):
        if algorithmList[i]:
            any += 1
            if algorithmList[i] == r - l:
                all += 1
    E = max(E, (any - all) * (r - l))
    for i in studentList[l][1]:
        algorithmList[i] -= 1
    l += 1
print(E)
