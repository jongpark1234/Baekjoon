db1 = ['', 'Yakk', 'Doh', 'Seh', 'Ghar', 'Bang', 'Sheesh']
db2 = ['', 'Habb Yakk', 'Dobara', 'Dousa', 'Dorgy', 'Dabash', 'Dosh']
for i in range(int(input())):
    a, b = sorted(map(int, input().split()))
    temp = db2[a] if a == b else 'Sheesh Beesh' if [a, b] == [5, 6] else f'{db1[b]} {db1[a]}'
    print(f'Case {i + 1}: {temp}')
