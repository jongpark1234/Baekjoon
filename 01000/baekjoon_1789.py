from sys import stdin
temp, s = 0, int(stdin.readline())
while True:
    temp += 1
    s -= temp
    if s < 0:
        print(temp - 1)
        break
