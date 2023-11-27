n = int(input())
result, temp = 0, 1
while temp <= int(n ** 0.5):
    if n % temp == 0:
        result += 2
    temp += 1
print(result - ((temp - 1) ** 2 == n))
