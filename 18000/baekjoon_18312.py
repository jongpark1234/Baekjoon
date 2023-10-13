result = 0
n, k = map(int, input().split())
for a in range(n + 1):
    for b in range(60):
        for c in range(60):
            if str(k) in (str(a).zfill(2) + str(b).zfill(2) + str(c).zfill(2)):
                result += 1
print(result)
