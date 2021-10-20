n = int(input())
times, temp, i = 0, 0, 0
while True:
    if str(i).count('666') >= 1:
        times += 1
    temp = i
    if times == n:
        break
    i += 1
print(temp)
