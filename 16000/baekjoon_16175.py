for _ in range(int(input())):
    n, m = map(int, input().split())
    candidates = [0 for _ in range(n)]
    for _ in range(m):
        v = list(map(int, input().split()))
        for i in range(n):
            candidates[i] += v[i]
    print(candidates.index(max(candidates)) + 1)
