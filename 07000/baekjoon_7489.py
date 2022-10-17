from math import factorial
for _ in range(int(input())):
    print(str(factorial(int(input()))).rstrip('0')[-1])
