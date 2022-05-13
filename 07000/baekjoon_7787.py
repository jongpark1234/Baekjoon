ret = 0
for i in map(int, input().split()):
    ret ^= bin(i)[2:][::-1].index('1') + 1
print('BA'[bool(ret)], 'player wins')
