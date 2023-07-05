numlist = []
for i in [*open(0)]:
    numlist.extend(list(map(int, i.split()[1:])))
print(min(numlist), max(numlist))
