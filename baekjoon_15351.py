for _ in range(int(input())):
    score = 0
    for i in input():
        if i != ' ':
            score += ord(i) - 64
    print('PERFECT LIFE' if score == 100 else score)
