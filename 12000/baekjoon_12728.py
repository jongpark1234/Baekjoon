result = [0, 6, 28]
for i in range(3, 1005001):
    result.append(((result[i - 1] * 6 - result[i - 2] * 4) + 10000) % 1000)
for i in range(int(input())):
    n = int(input())
    print(f'Case #{i + 1}: {((result[n] if n < 105 else result[(n - 4) % 100 + 4]) + 999) % 1000:03d}')
