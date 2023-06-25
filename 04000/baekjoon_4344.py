def roundTraditional(val, digits):
    return round(val + 10 ** (-len(str(val)) - 1), digits)
for i in range(int(input())):
    n, *scores = map(int, input().split())
    print(f'{roundTraditional((sum(map(lambda x: x > sum(scores) / n, scores)) / n) * 100, 3):.3f}%')
