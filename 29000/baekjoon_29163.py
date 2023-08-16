n = int(input())
a = sum(map(lambda x: int(x) % 2 * 2 - 1, input().split()))
print('Sad' if a >= 0 else 'Happy')
