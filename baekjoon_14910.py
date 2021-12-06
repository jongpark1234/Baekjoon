numlist = list(map(int, input().split()))
print('Good' if numlist == sorted(numlist) else 'Bad')
