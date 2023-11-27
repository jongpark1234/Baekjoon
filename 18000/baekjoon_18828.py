n = int(input())
ret, num = 0, 1
while num <= int(n ** 0.5):
    if n % num == 0:
        ret += 2
    num += 1
if (num - 1) ** 2 == n:
    ret -= 1
print(ret)
