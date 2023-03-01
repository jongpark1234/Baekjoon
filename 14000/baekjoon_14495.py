fibonacci = [1, 1, 1]
for i in range(2, 117):
    fibonacci.append(fibonacci[i - 2] + fibonacci[i])
print(fibonacci[int(input()) - 1])
