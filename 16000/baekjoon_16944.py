condition = ['0123456789', 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!@#$%^&*()-+']
satisfy = [0, 0, 0, 0]
cnt = 0
n = int(input())
password = input()
for i in password:
    for j in range(4):
        if i in condition[j]:
            satisfy[j] = 1
for i in range(4):
    if satisfy[i] == 0:
        cnt += 1
if n + cnt >= 6:
    print(cnt)
else:
    print(6 - n)
