num = [input() for _ in range(4)]
if num[0] in '89' and num[3] in '89' and num[1] == num[2]:
    print('ignore')
else:
    print('answer')
