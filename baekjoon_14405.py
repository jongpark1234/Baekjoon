s = input()
while s.count('pi') or s.count('ka') or s.count('chu'):
    s = s.replace('pi', ' ', 1)
    s = s.replace('ka', ' ', 1)
    s = s.replace('chu', ' ', 1)
print('NO' if len(s.strip()) else 'YES')
