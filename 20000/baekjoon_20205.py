n, k = map(int, input().split())
print('\n'.join(map(lambda x: '\n'.join(' '.join(map(lambda y: ' '.join(y), x)) for _ in range(k)), [list(map(lambda x: list(x * k), input().split())) for _ in range(n)])))
