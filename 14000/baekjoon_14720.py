turn = result = 0
n = int(input())
for i in map(int, input().split()):
    if i == turn:
        turn = (turn + 1) % 3
        result += 1
print(result)
