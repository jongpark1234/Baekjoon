for _ in range(int(input())):
    color = count = False
    g1, s1, b1, g2, s2, b2 = map(int, input().split())
    if g1 + s1 + b1 > g2 + s2 + b2:
        count = True
    if g1 > g2 or (g1 == g2 and s1 > s2) or (g1 == g2 and s1 == s2 and b1 > b2):
        color = True
    print(g1, s1, b1, g2, s2, b2)
    print('both' if count and color else 'color' if color else 'count' if count else 'none', end='\n\n')
