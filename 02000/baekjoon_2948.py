from datetime import date
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
d, m = map(int, input().split())
print(weekdays[date(2009, m, d).weekday()])
