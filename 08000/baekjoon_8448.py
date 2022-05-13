x, y, z = [], [], []
maxnums = [-1e21 for _ in range(8)]
n = int(input())
for i in range(n):
    Input = [*map(int, input().split())]
    x.append(Input[0])
    y.append(Input[1])
    z.append(Input[2])
    for j in range(8):
        ret = 0
        ret += x[i] if j & 1 else -x[i]
        ret += y[i] if j & 2 else -y[i]
        ret += z[i] if j & 4 else -z[i]
        maxnums[j] = max(maxnums[j], ret)
for i in range(n):
    result = 0
    for j in range(8):
        ret = 0
        ret += x[i] if j & 1 else -x[i]
        ret += y[i] if j & 2 else -y[i]
        ret += z[i] if j & 4 else -z[i]
        result = max(result, maxnums[j] - ret)
    print(result)
