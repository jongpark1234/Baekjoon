depth = [int(input()) for _ in range(4)]
if len(set(depth)) == 1:
    print('Fish At Constant Depth')
elif len(set(depth)) != 4:
    print('No Fish')
elif depth == sorted(depth):
    print('Fish Rising')
else:
    print('Fish Diving')
