from sys import stdin, maxsize
n = int(stdin.readline())
value = list(map(int, stdin.readline().split()))
distance = maxsize
l, r = 0, n - 1
while l < r:
    solution = value[l] + value[r]
    if abs(solution) < distance:
        result = solution
        distance = abs(solution)
    if solution < 0:
        l += 1
    elif solution > 0:
        r -= 1
    else:
        break
print(result)
