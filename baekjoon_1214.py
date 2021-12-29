d, p, q = map(int, input().split())
p, q = max(p, q), min(p, q)
if d % p == 0 or d % q == 0:
    print(d)
    exit(0)
else:
    result = d // p * p + p
temp = result
for i in range(1, temp // p + 1):
    new_result = temp - p * i
    if (d - new_result) % q == 0:
        print(d)
        exit(0)
    else:
        new_result += ((d - new_result) // q) * q + q
    if result == new_result:
        break
    result = min(result, new_result)
print(result)
