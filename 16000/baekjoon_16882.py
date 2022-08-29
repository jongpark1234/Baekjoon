n = int(input())
x = list(map(int, input().split()))
card = set(x)
for i in card:
    if x.count(i) & 1:
        print('koosaga')
        break
else:
    print('cubelover')
