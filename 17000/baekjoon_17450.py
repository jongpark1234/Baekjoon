snack = [list(map(int, input().split())) for _ in range(3)]
result = [(i[1] * 10) / (i[0] * 10 - (500 if i[0] > 499 else 0)) for i in snack]
print('SNU'[result.index(max(result))])
