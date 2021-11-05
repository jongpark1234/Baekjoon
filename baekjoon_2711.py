for _ in range(int(input())):
    num, s = input().split()
    print(s[:int(num) - 1] + s[int(num):])
