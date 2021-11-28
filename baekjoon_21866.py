hacker = False
criteria = [100, 100, 200, 200, 300, 300, 400, 400, 500]
scorelist = list(map(int, input().split()))
for i in range(9):
    if scorelist[i] > criteria:
        hacker = True
        break
if hacker:
    print('hacker')
elif sum(scorelist) < 100:
    print('none')
else:
    print('draw')
