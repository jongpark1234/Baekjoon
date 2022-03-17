from functools import cmp_to_key
k, n = map(int, input().split())
a = [int(input()) for _ in range(k)]
big = max(a)
for _ in range(k, n):
    a.append(big)
print(''.join(map(str, sorted(a, key = cmp_to_key(lambda x, y: int(str(y) + str(x)) - int(str(x) + str(y)))))))
