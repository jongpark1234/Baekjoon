a, b = map(int, input().split())
result = 1
while True:
    if a == b:
        break
    elif (b % 2 and b % 10 != 1) or (a > b):
        result = -1
        break
    else:
        if b % 10 == 1:
            b //= 10
            result += 1
        else:
            b //= 2
            result += 1
print(result)
