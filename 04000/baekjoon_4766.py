temp = float('inf')
while (n := float(input())) != 999:
    if temp == float('inf'):
        temp = n
        continue
    print(f'{n - temp:.2f}')
    temp = n
