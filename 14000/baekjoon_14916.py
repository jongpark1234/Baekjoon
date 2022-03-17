n = int(input())
count = 0
while True:
    if n < 0:
        count = -1
        break
    elif n % 5 == 0:
        count += n // 5
        break
    n -= 2
    count += 1
print(count)
