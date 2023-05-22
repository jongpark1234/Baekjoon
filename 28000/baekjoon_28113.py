n, a, b = map(int, input().split())
print('Bus' if a < b or b < n else 'Subway' if a > b else 'Anything')
