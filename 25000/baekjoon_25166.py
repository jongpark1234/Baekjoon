money = 0b1111111111
s, m = map(int, input().split())
print('No thanks' if money & s == s else 'Thanks' if (s - money) & m == (s - money) else 'Impossible')
