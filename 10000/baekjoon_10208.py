for i in range(int(input())):
    result = 0
    w, c, d = map(int, input().split())
    strength = [0 for _ in range(111)]
    for j in range(1, d + 1):
        strength[j] = w
    for j in range(1, d + 1):
        g, s = map(int, input().split())
        for k in range(j + 1, j + 3):
            strength[k] -= s
        for k in range(j + 3, d + 1):
            strength[k] += g
    for j in range(1, d + 1):
        if strength[j] < c + j - 1:
            result = j
            break
    print(f'Data Set {i + 1}:')
    print(result if result else 'Completed successfully.', end = '\n\n')
