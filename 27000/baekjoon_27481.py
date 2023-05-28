result = 0
n = int(input())
for i in input():
    if i.isnumeric():
        result ^= (1 << int(i))
    else:
        for j in range(10) if i == 'L' else range(9, -1, -1):
            if ~result & (1 << j):
                result |= (1 << j)
                break
print(bin(result)[2:][::-1].ljust(10, '0'))
