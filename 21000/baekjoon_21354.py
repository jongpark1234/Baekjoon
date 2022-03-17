a, p = map(int, input().split())
a *= 7
p *= 13
if a > p:
    print('Axel')
elif p > a:
    print('Petra')
else:
    print('lika')
