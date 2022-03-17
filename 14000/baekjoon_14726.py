for _ in range(int(input())):
    card = list(input())
    for i in range(len(card)):
        if not i % 2:
            card[i] = str(int(card[i]) * 2)
            if int(card[i]) >= 10:
                card[i] = str(int(card[i][0]) + int(card[i][1]))
    print('F' if sum(map(int, card)) % 10 else 'T')
