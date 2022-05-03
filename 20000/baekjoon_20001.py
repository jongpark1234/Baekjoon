problems = 0
input()
while True:
    line = input()
    if line == "고무오리 디버깅 끝":
        break
    if line == '문제':
        problems += 1
    if line == '고무오리':
        problems += 2 if problems == 0 else -1
print('고무오리야 사랑해' if problems == 0 else '힝구')
