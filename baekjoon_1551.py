n, k = map(int, input().split())
seq = list(map(int, input().split(',')))
for i in range(k):
    seq = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
print(','.join(map(str, seq)))
