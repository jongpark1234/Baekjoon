from functools import cmp_to_key
result = []
while True:
    try:
        result.append(input())
    except:
        break
print(int(''.join(sorted(result, key = cmp_to_key(lambda x, y: 1 if int(x + y) < int(y + x) else -1)))))
