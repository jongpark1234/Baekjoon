def cycling(x):
    return int(str(x)[-1] + str(sum(list(map(int, str(x)))))[-1])
n = int(input())
num, cycle = n, 0
while True:
    if (num < 10):
        num = int('0' + str(num))
    cycle += 1
    num = cycling(num)
    if num == n:
        break
print(cycle)

