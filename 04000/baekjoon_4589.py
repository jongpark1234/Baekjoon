print('Gnomes:')
for _ in range(int(input())):
    print(['Uno','O'][(a:=[*map(int, input().split())]) in [sorted(a), sorted(a, reverse = True)]] + 'rdered')
