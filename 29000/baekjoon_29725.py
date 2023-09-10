s = ' '.join([*open(0)])
print(
    s.count('P') * 1 + s.count('N') * 3 + s.count('B') * 3 + s.count('R') * 5 + s.count('Q') * 9 -
    (s.count('p') * 1 + s.count('n') * 3 + s.count('b') * 3 + s.count('r') * 5 + s.count('q') * 9)
)
