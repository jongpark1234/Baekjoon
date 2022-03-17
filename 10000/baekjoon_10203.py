for _ in range(int(input())):
    s = input()
    cnt = 0
    for i in s:
        if i in 'aeiouAEIOU':
            cnt += 1
    print(f'The number of vowels in {s} is {cnt}.')
