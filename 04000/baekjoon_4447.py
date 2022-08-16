for _ in range(int(input())):
    name = input()
    g, b = name.lower().count('g'), name.lower().count('b')
    print(name, 'is', ['A BADDY', 'NEUTRAL', 'GOOD'][2 if g > b else 1 if g == b else 0])
