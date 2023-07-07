from math import *
for _ in range(int(input())):
    result = 0
    for i in range(int(input())):
        result += log10(i + 1)
    print(int(result) + 1)
