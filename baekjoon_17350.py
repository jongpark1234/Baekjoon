import sys
n = int(sys.stdin.readline())
anj = False
for i in range(n):
    player = sys.stdin.readline().rstrip()
    if player == 'anj':
        anj = True
print('뭐야', end='')
if anj: print(';')
else: print('?')
