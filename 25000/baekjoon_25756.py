v = 0
n = int(input())
for i in map(int, input().split()):
    v = (1 - (1 - v / 100) * (1 - i / 100)) * 100
    print(v)
