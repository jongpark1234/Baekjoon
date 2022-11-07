n, p, h = map(int, input().split())
for _ in range(n):
    d = int(input())
    if d < p:
        print(f'NTV: Dollar dropped by {p - d} Oshloobs')
    elif d > h:
        h = d
        print(f'BBTV: Dollar reached {h} Oshloobs, A record!')
    p = d
