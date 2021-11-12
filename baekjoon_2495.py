for i in range(3):
    s = input()
    total = 0
    continuous = 1
    now = s[0]
    for j in range(1, 8):
        if now == s[j]:
            continuous += 1
        else:
            continuous = 1
        total = max(continuous, total)
        now = s[j]
    print(total)
