cur = 0
n, d = map(int, input().split())
print('+---------------------+')
while cur != n:
    row = ''
    for j in range(7):
        if d > 1 or cur == n:
            d -= 1
            row += '...'
        else:
            cur += 1
            row += str(cur).rjust(3, '.') 
    print('|' + row + '|')
print('+---------------------+')
