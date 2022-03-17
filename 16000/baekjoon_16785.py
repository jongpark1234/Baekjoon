a, b, c = map(int, input().split())
coin, login = 0, 0
while coin < c:
    login += 1
    coin += a
    if login % 7 == 0:
        coin += b
print(login)
