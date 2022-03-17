from sys import stdin
n = int(stdin.readline())
puzzle1 = list(map(int, stdin.readline().split()))
puzzle2 = list(map(int, stdin.readline().split()))
ind = puzzle2.index(puzzle1[0])
front = puzzle2[ind:] + puzzle2[:ind]
ind = puzzle2[::-1].index(puzzle1[0])
back = puzzle2[::-1][ind:] + puzzle2[::-1][:ind]
print('good puzzle' if puzzle1 == front or puzzle1 == back else 'bad puzzle')
