n = int(input())
def bottle(n, lower=False):
    return f'{"n" if lower else "N"}o more bottles' if n == 0 else '1 bottle' if n == 1 else f'{n} bottles'
for i in range(n, -1, -1):
    print(f'{bottle(i)} of beer on the wall, {bottle(i, True)} of beer.')
    print(f'Take one down and pass it around, {bottle(i - 1, True)} of beer on the wall.' if i else f'Go to the store and buy some more, {bottle(n)} of beer on the wall.')
    print()
