n = int(input())
a = list(map(int, input()))
b = list(map(int, input()))
if n % 2:
    for i in range(len(a)):
        a[i] ^= 1
print('Deletion succeeded' if a == b else 'Deletion failed')
