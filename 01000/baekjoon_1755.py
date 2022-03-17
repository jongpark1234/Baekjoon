keyword = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
dictlist = []
m, n = map(int, input().split())
numlist = [i for i in range(m, n + 1)]
for i in numlist:
    word = ''
    for j in str(i):
        word += keyword[int(j)]
    dictlist.append([word, i])
dictlist.sort()
for i in range(len(dictlist)):
    if i % 10 == 0 and i != 0:
        print()
    print(dictlist[i][1], end=' ')
