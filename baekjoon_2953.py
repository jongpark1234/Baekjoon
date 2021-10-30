numlist = []
for i in range(5):
    numlist.append(sum(list(map(int, input().split()))))
print(numlist.index(max(numlist)) + 1, max(numlist))
