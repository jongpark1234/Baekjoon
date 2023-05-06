for _ in range(int(input())):
    s = input()
    cnt = [0, 0]
    for i in s:
        cnt[i in 'aeiou'] += 1
    print(s)
    print(+(cnt[1] > cnt[0]))
