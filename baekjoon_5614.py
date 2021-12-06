from sys import stdin
input = stdin.readline
product = [input().split() for _ in range(int(input()))]
products = {}
result = []
for i in product:
    try:
        products[i[0]] += int(i[1])
    except KeyError:
        products[i[0]] = int(i[1])
for i in products.keys():
    result.append([i, products[i]])
for i in sorted(result, key = lambda x: (len(x[0]), x[0])):
    print(*i)
