for _ in range(int(input())):
    n = int(input())
    pairs = []
    for i in range(1, n // 2 + 1):
        if i == n - i:
            break
        pairs.append(f'{i} {n - i}')
    print('Pairs for', str(n) + ':', ', '.join(pairs))
