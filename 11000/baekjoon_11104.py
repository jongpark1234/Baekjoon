for _ in range(int(input())):
    n = input()
    result, temp = 0, 1
    for i in n[::-1]:
        result += temp * int(i)
        temp <<= 1
    print(result)
