a, b, c = map(int, input().split())
print('*' if a == b == c else 'C' if a == b else 'A' if b == c else 'B')
