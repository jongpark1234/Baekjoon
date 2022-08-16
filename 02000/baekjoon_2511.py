alist = list(map(int, input().split()))
blist = list(map(int, input().split()))
a = b = 0
winner = 'D'
for i in range(10):
    if alist[i] > blist[i]:
        a += 3
        winner = 'A'
    elif alist[i] < blist[i]:
        b += 3
        winner = 'B'
    else:
        a += 1
        b += 1
print(a, b)
print(f'{winner}BA'[(a != b) + (a > b)])
