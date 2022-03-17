n = int(input())
for i in range(n):
    mars = input().split()
    number = float(mars[0])
    for j in range(1, len(mars)):
        if mars[j] == '@':
            number *= 3
        elif mars[j] == '%':
            number += 5
        elif mars[j] == '#':
            number -= 7
    print('{:.2f}'.format(number))
