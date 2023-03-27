n, k = map(int, input().split())
fk, f2k = str(k)[-1], str(k << 1)[-1]
results = [i for i in range(1, n + 1) if (temp := str(i)[-1]) != fk and temp != f2k]
print(len(results))
print(*results)
