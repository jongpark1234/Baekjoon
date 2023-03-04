l = int(input())
w = int(input())
h = int(input())
print('good' if min(l, w) >= h * 2 and max(l, w) <= min(l, w) * 2 else 'bad')
