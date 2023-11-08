print(max(result := list(map(lambda x: x.count('1'), map(lambda y: __import__('re').sub(r'(.)\1*', lambda z: z.group(1), y.strip()).split('0'), [*open(0)][1:])))), result.count(max(result)))
