isbn = [9, 7, 8, 0, 9, 2, 1, 4, 1, 8] + [int(input()) for i in range(3)]
Sum = 0
for i in range(13):
    if i % 2:
        Sum += isbn[i] * 3
    else:
        Sum += isbn[i] * 1
print(f'The 1-3-sum is {Sum}')
