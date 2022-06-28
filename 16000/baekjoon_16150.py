for i in range(int(input())):
    n, m = map(int, input().split())
    b, c, result = [0], [0], [0] + [float('inf') for _ in range(m + 1)]
    for _ in range(n):
        Input = list(map(int, input().split()))
        b.append(Input[0])
        c.append(Input[1])
    for j in range(1, n + 1):
        b[j] = min(b[j], m + 1)
        for k in range(m - b[j] + 1, m + 2):
            if result[k] + c[j] < result[m + 1]:
                result[m + 1] = result[k] + c[j]
        for k in range(b[j], m + 1)[::-1]:
            if result[k - b[j]] + c[j] < result[k]:
                result[k] = result[k - b[j]] + c[j]
    print(f'Data Set {i + 1}:\n{result[m + 1]}\n')
