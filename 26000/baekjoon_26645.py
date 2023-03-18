n = int(input())
results = [min(max(240 - n - i * 10, 0), 1 << i) for i in range(4)]
print(4 - results.index(max(results)))
