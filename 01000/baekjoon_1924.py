days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
x, y = map(int, input().split())
day = 0
for i in range(1, x):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
       day += 31
    elif i == 2:
        day += 28
    else:
        day += 30
day += y
print(days[day % 7 - 1])
