for _ in range(int(input())):
    d = int(input())
    for i in range(999):
        if i + i * i > d:
            print(i - 1)
            break
