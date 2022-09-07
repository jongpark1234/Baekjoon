n, m = map(int, input().split())
print(''.join(map(str, [i % 5 + 1 for i in range(n)])))
