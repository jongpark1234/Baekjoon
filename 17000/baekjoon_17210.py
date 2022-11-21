x = int(input())
y = int(input())
print('Love is open door' if x > 5 else '\n'.join(map(str, [(y := y ^ 1) for _ in range(x - 1)])))
