n = int(input())
piece = 1
a = 1
for i in range(n):
    piece += a
    if i % 2 == 0: a += 1
print(piece)
