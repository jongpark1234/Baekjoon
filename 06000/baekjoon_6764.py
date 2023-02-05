depth = [int(input()) for _ in range(4)]
if len(set(depth)) == 1:
    print('Fish At Constant Depth')
elif len(set(depth)) == 4:
    if depth == sorted(depth):
        print('Fish Rising')
    elif depth == sorted(depth, reverse=True):
        print('Fish Diving')
    else:
        print('No Fish')
else:
    print('No Fish')
