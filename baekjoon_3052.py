num = []
for i in range(10):
    num.append(int(input()))
    num[i] %= 42
print(len(list(set(num))))