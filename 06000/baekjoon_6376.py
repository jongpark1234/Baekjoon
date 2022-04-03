from math import factorial
e = 0
print('n e\n- -----------')
for n in range(10):
    e += factorial(n) ** -1
    if n < 2:
        print(f'{n} {e:.0f}')
    elif n == 2:
        print(f'{n} {e:.1f}')
    else:
        print(f'{n} {e:.9f}')
