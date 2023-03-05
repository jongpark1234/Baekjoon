for _ in range(int(input())):
    area, base = map(float, input().split())
    print(f'The height of the triangle is {area / base * 2:.2f} units')
