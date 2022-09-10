for i in [*map(int, open(0))][1:]:
    result = -float('inf')
    while i != 1:
        result = max(result, i)
        i = i * 3 + 1 if i & 1 else i >> 1
    print(max(result, i))
