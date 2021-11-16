fibonacci = []
for i in range(int(input()) + 1):
    if i == 0:
        temp = 0
    elif i <= 2:
        temp = 1
    else:
        temp = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(temp)
print(fibonacci[-1])
