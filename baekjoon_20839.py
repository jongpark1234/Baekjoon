a1, c1, e1 = map(float, input().split())
a2, c2, e2 = map(float, input().split())
if a2 >= a1 and c2 >= c1 and e2 >= e1:
    print('A')
    exit(0)
if a2 >= a1 / 2 and c2 >= c1 and e2 >= e1:
    print('B')
    exit(0)
if c2 >= c1 and e2 >= e1:
    print('C')
    exit(0)
if c2 >= c1 / 2 and e2 >= e1 / 2:
    print('D')
    exit(0)
print('E')
