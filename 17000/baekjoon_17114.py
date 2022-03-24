# pypy3
from sys import stdin
from collections import deque
day = 0
m, n, o, p, q, r, s, t, u, v, w = map(int, stdin.readline().split())
queue = deque([])
dm = [1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dn = [0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
do = [0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dp = [0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dq = [0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ds = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0]
dt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0]
du = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0]
dv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0]
dw = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1]
hyperStorage = [[[[[[[[[[list(map(int, stdin.readline().split())) for _ in range(n)] for _ in range(o)] for _ in range(p)] for _ in range(q)] for _ in range(r)] for _ in range(s)] for _ in range(t)] for _ in range(u)] for _ in range(v)] for _ in range(w)]
for W in range(w):
    for V in range(v):
        for U in range(u):
            for T in range(t):
                for S in range(s):
                    for R in range(r):
                        for Q in range(q):
                            for P in range(p):
                                for O in range(o):
                                    for N in range(n):
                                        for M in range(m):
                                            if hyperStorage[W][V][U][T][S][R][Q][P][O][N][M] == 1:
                                                queue.append([W, V, U, T, S, R, Q, P, O, N, M])
while queue:
    W, V, U, T, S, R, Q, P, O, N, M = queue.popleft()
    for i in range(22):
        nw, nv, nu, nt, ns, nr, nq, np, no, nn, nm = dw[i] + W, dv[i] + V, du[i] + U, dt[i] + T, ds[i] + S, dr[i] + R, dq[i] + Q, dp[i] + P, do[i] + O, dn[i] + N, dm[i] + M
        if 0 <= nw < w and 0 <= nv < v and 0 <= nu < u and 0 <= nt < t and 0 <= ns < s and 0 <= nr < r and 0 <= nq < q and 0 <= np < p and 0 <= no < o and 0 <= nn < n and 0 <= nm < m and hyperStorage[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] == 0:
            hyperStorage[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] = hyperStorage[W][V][U][T][S][R][Q][P][O][N][M] + 1
            queue.append([nw, nv, nu, nt, ns, nr, nq, np, no, nn, nm])
for W in hyperStorage:
    for V in W:
        for U in V:
            for T in U:
                for S in T:
                    for R in S:
                        for Q in R:
                            for P in Q:
                                for O in P:
                                    for N in O:
                                        for M in N:
                                            if M == 0:
                                                print(-1)
                                                exit(0)
                                        day = max(day, max(N))
print(day - 1)
