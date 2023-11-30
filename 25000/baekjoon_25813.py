s = input()
print('-' * s.index('U') + 'U' + 'C' * (s.rindex('F') - s.index('U') - 1) + 'F' + '-' * (len(s) - s.rindex('F') - 1))
