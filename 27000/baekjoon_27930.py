yonsei = korea = 0
s = input()
for i in s:
    if i == 'YONSEI'[yonsei]:
        yonsei += 1
    if i == 'KOREA'[korea]:
        korea += 1
    if yonsei == 6:
        print('YONSEI')
        break
    if korea == 5:
        print('KOREA')
        break
