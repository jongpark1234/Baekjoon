n, u, l = map(int, input().split())
f1, f2 = n > 999, u > 7999 or l > 259
print('Very Good' if f1 and f2 else 'Good' if f1 else 'Bad')
