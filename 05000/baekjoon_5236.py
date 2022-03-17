for _ in range(int(input())):
    s = input()
    result = ''
    for i in s[::-1]:
        try:
            if i > result[-1]:
                result += i
            else:
                break
        except:
            result += i
    print(f'The longest decreasing suffix of {s} is {result[::-1]}')
