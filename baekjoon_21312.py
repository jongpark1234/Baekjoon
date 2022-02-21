a, b, c = map(int, input().split())
cocktail = sorted([a, b, c, a * b, b * c, a * c, a * b * c], key= lambda x: (x % 2 == 0, -x))
print(cocktail[0])
