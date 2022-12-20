for _ in range(int(input())):
    result = 0
    for _ in range(int(input())):
        name, count, price = input().split()
        result += float(price) * int(count)
    print(f'${result:.2f}')
