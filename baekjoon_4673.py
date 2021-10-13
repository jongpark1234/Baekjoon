num = 0
numlist = []
while True:
    num += 1
    i = 0
    temp = num + sum(list(map(int, str(num))))
    if num > 10000:
        break
    else:
        numlist.append(temp)
for i in range(1, 10001):
    if numlist.count(i) == 0:
        print(i)