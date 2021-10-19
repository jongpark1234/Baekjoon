n, m = map(int, input().split())
if m == 1 or m == 2: print('NEWBIE!')
elif m <= n: print('OLDBIE!')
else: print('TLE!')
