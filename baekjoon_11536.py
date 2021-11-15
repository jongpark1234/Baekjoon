from sys import stdin
players = []
for i in range(int(stdin.readline())):
    players.append(stdin.readline().rstrip())
if players == sorted(players, reverse=True): print('DECREASING')
elif players == sorted(players): print('INCREASING')
else: print('NEITHER')
