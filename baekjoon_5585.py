n = 1000 - int(input())
cnt = 0
money = [500, 100, 50, 10, 5, 1]
for i in money:
    cnt += n // i
    n %= i
print(cnt)
