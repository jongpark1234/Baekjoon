a, b = input().split()
if a.isdecimal() and b.isdecimal():
    print(int(a) - int(b))
else:
    print('NaN')
