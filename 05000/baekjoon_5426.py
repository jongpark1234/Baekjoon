from math import isqrt
for _ in range(int(input())):
    s = input()
    length = isqrt(len(s))
    print(''.join(map(lambda x: ''.join(x), reversed(list(zip(*[s[i * length:(i + 1) * length] for i in range(length)]))))))
