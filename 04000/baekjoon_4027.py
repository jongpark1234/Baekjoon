tc = 0
while True:
    src = []
    dist = []
    em = [False for _ in range(1000)]
    cost = [0 for _ in range(1000)]
    try:
        n, character1, character2 = input().split()
    except:
        break
    tc += 1
    n = int(n)
    for i in range(n):
        src.append(int(character1[i]))
        dist.append(int(character2[i]))
    s = r = t = m = start = change = nchange = result = 0
    ith = [*map(int, input().split())]
    for i in range(n):
        if src[i] or dist[i]:
            if src[i]:
                t += ith[i]
                if not dist[i]:
                    s += ith[i]
                else:
                    r += ith[i]
            elif dist[i]:
                s += ith[i]
            if src[i] != dist[i]:
                nchange += 1
            j = m
            savedSrc = src[i]
            savedDist = dist[i]
            while j > 0 and cost[j - 1] < ith[i]:
                cost[j] = cost[j - 1]
                src[j] = src[j - 1]
                dist[j] = dist[j - 1]
                j -= 1
            cost[j] = ith[i]
            src[j] = savedSrc
            dist[j] = savedDist
            m += 1
        em[i] = False
    for i in range(m):
        if src[i]:
            if not dist[i]:
                s -= cost[i]
                nchange -= 1
            else:
                change += r * 2 - cost[i] + s - nchange * cost[i]
                if change < 0:
                    for j in range(start, i + 1):
                        if src[j] and dist[j]:
                            em[j] = True
                    change = 0
                    start = i + 1
                r -= cost[i]
        else:
            s -= cost[i]
            nchange -= 1
    for i in range(m):
        if src[i]:
            if not dist[i] or em[i]:
                t -= cost[i]
                result += t
    for i in range(m)[::-1]:
        if not src[i] or em[i]:
            t += cost[i]
            result += t
    print(f'Case {tc}: {result}')
