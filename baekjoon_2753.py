year = int(input())
leap = 0
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap = 1
print(leap)