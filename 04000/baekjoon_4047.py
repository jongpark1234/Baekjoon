t = 0
MAX = 100
cards = [[0, False] for _ in range(MAX)]
while (n := int(input())) != 0:
    t += 1
    left = 0
    right = n - 1
    character = input()
    for i in range(n):
        cards[i][0] = i + 1
        cards[i][1] = character[i] == 'U'
    character = input()
    for i in range(n - 1):
        if character[i] == 'L':
            for j in range(left // 2 + 1):
                cards[j], cards[left - j] = cards[left - j], cards[j]
            for j in range(left + 1):
                cards[j][1] = not cards[j][1]
            left += 1
        else:
            k = n - 1
            j = right
            while j < k:
                cards[j], cards[k] = cards[k], cards[j]
                j += 1
                k -= 1
            for j in range(right, n):
                cards[j][1] = not cards[j][1]
            right -= 1
    if character[-1] == 'L':
        k = n - 1
        j = right
        while j < k:
            cards[j], cards[k] = cards[k], cards[j]
            j += 1
            k -= 1
    else:
        for j in range(left // 2 + 1):
            cards[j], cards[left - j] = cards[left - j], cards[j]
        for j in range((n - 1) // 2 + 1):
            cards[j], cards[n - j - 1] = cards[n - j - 1], cards[j]
    print(f'Pile {t}')
    for q in [*map(int, input().split())][1:]:
        print(f'Card {q} is a face', 'up' if cards[q - 1][1] else 'down', f'{cards[q - 1][0]}.')
