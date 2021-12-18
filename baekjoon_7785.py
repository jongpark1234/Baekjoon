from sys import stdin
company = {}
for i in range(int(stdin.readline())):
    name, access = stdin.readline().rstrip().split()
    if access == 'enter':
        company[name] = 1
    else:
        del company[name]
s = sorted(company.keys(), reverse=True)
print('\n'.join(s))
