result = 0
x = int(input())
for _ in range(int(input())):
    result += x
    p = int(input())
    result = max(result - p, 0)
print(result + x)
