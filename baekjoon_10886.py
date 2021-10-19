n = int(input())
survey = [0, 0]
iscute = ''
for i in range(n):
    s = int(input())
    if s == 0: survey[0] += 1
    else: survey[1] += 1
if survey[0] > survey[1]: iscute = 'not '
else: iscute = ''
print('Junhee is ' + iscute + 'cute!')
