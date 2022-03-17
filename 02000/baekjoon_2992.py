import itertools
x = input()
s = list(itertools.permutations(sorted(list(x)), len(x)))
for i in s:
    if int(''.join(i)) > int(x):
        print(''.join(i))
        find = 0
        break
try:
    find += 1
except:
    print(0)
