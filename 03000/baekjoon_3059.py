for _ in range(int(input())):
    s = list(input())
    result = 0
    for i in range(65, 91):
        if chr(i) not in s:
            result += i
    print(result)
