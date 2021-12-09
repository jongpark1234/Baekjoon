outcome = ''
for i in range(6):
    outcome += input()
if outcome == 'LLLLLL':
    print(-1)
else:
    print('332211'[outcome.count('W') - 1])
