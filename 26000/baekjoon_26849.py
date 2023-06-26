numlist = [eval('/'.join(i.split())) for i in [*open(0)][1:]]
print(min(numlist), max(numlist), sum(numlist))
