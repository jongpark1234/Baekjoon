# from sys import stdin, setrecursionlimit
# from math import ceil, log2
# setrecursionlimit(10 ** 5)
# def dfs(x,z):
#     global cnt
#     cnt += 1
#     pre[x] = cnt
#     depth[x] = z
#     for nx in child[x]:
#         if pre[nx] == -1:
#             dfs(nx, z + 1)
#     post[x] = cnt
# def A1(n, s, e, i):
#     if s > i or e < i:
#         return tank[n]
#     if s == e:
#         tank[n] += 1
#         return tank[n]
#     mid = (s + e) // 2
#     tank[n] = A1(n * 2, s, mid, i) + A1(n * 2 + 1, mid + 1, e, i)
#     return tank[n]
# def A2(n, s, e, L, R):
#     if s > R or e < L:
#         return False
#     if L <= s and e <= R:
#         return tank[n]
#     mid = (s + e) // 2
#     return A2(n * 2, s, mid, L, R) + A2(n * 2 + 1, mid + 1, e, L, R)
# cnt = -1
# n, c = map(int, stdin.readline().split())
# h = int(ceil(log2(n)))
# child = [[] for _ in range(n)]
# pre = [-1 for _ in range(n)]
# post = [-1 for _ in range(n)]
# depth = [-1 for _ in range(n)]
# tank = [0 for _ in range(1 << (h + 1))]
# for i in range(n - 1):
#     a, b =map(int, stdin.readline().split())
#     a -= 1
#     b -= 1
#     child[a].append(b)
#     child[b].append(a)
# dfs(c - 1, 1)
# for _ in range(int(stdin.readline())):
#     a, b = map(int, stdin.readline().split())
#     b -= 1
#     if a == 1:
#         A1(1, 0, n - 1, pre[b])
#     else:
#         print(A2(1, 0, n - 1, pre[b], post[b]) * depth[b])
print(10 ** 5)