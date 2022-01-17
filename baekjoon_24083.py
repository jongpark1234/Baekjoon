a = int(input())
b = int(input())
time = (a + b % 12) % 12
print(12 if time == 0 else time)
