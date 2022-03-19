from sys import stdin
def g(a):
    for i in a:
        if i % 2:
            return False
    return True
ret = 0
a = [int(stdin.readline()) for _ in range(int(stdin.readline()))]
for i in a:
    ret ^= i
if ret > 1:
    print('Alice')
elif ret == 1:
    print('Bob')
else:
    print('Bob' if g(a) else 'Alice')
