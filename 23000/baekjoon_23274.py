from math import hypot
Input = list(map(int, input().split()))
print(max(hypot(Input[0] - Input[2], Input[1] - Input[3]), hypot(Input[4] - Input[6], Input[5] - Input[7])))
