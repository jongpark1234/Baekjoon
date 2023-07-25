for _ in range(int(input())):
    s = input()
    length = len(s)
    print(s)
    for i in range(length - 2):
        print(s[i + 1] + ' ' * (length - 2) + s[length - i - 2])
    if length > 1:
        print(s[::-1])
