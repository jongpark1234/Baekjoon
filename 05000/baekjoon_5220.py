for _ in range(int(input())):
    n, check = map(int, input().split())
    print('Valid' if bin(n)[2:].count('1') % 2 == check else 'Corrupt')
