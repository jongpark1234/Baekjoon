a, b = map(int, input().split())
crystal = 0
if b == 0:
    crystal = 1
elif b == 1:
    crystal = a
else:
    crystal = a
    temp = crystal
    for i in range(b - 1):
        temp += a - 2
        crystal += temp - 1 
print(crystal)
        