import sys
notation = ''
n = int(sys.stdin.readline())
for _ in range(n * 2 - 1):
    notation += sys.stdin.readline().rstrip()
notation = notation.replace('/', '//')
print(eval(notation))
