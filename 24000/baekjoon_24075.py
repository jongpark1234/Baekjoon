a, b = map(int, input().split())
print(max(a + b, a - b), min(a + b, a - b), sep='\n')
