seats = [['.' for _ in range(20)] for _ in range(10)]
for _ in range(int(input())):
    seat = input()
    row, col = ord(seat[0]) - 65, int(seat[1:]) - 1
    seats[row][col] = 'o'
print('\n'.join(map(lambda x: ''.join(x), seats)))
