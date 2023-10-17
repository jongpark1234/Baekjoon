print('JABCDEFGHIZ'[sum(i * j for i, j in zip(list(map(int, input())), [2, 7, 6, 5, 4, 3, 2])) % 11])
