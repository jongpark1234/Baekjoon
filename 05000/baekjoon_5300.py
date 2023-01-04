n = int(input())
for i in range(1, n + 1):
    print(i, end=' ')
    if i % 6 == 0:
        print('Go!', end=' ')
        if i == n:
            break
else:
    print('Go!')
