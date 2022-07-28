n, c = map(int, input().split())
result1 = result2 = temp = 0
for _ in range(n):
    ai, t = input().split()
    if t == 'bedroom':
        result2 += int(ai)
    if t == 'balcony':
        temp += int(ai)
    result1 += int(ai)
print(result1)
print(result2)
print(c * (result1 - temp / 2))
