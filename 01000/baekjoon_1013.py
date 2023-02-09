from re import compile
for _ in range(int(input())):
    print('YES' if compile('(100+1+|01)+').fullmatch(input()) else 'NO')
