from math import sqrt
while True:
    try:
        r, s = map(float, input().split())
        print(round(sqrt((r * (s + 0.16)) / 0.067)))
    except EOFError:
        break
