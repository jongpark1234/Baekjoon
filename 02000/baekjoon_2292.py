n = int(input())
room = 1
stack = 1
dis = 1
while True:
    if n <= room:
        break
    dis += 1
    stack = 6 * (dis - 1)
    room += stack
print(dis)