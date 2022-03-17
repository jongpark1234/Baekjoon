def powf(x):
    return pow(x, 2)
number = list(map(int, input().split()))
print(sum(list(map(powf, number))) % 10)