result = 0
for i in [*open(0)]:
    s, x = map(lambda x: int(x) if x.isnumeric() else x, i.split())
    result += x * (21 if s == 'Es' else 17)
print(result)
