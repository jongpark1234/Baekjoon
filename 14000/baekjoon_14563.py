def divisors(n):
    ret = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ret.append(i)
            if i ** 2 != n:
                ret.append(n // i)
    return sorted(ret)[:-1]
n = int(input())
for i in map(int, input().split()):
    temp = sum(divisors(i))
    print('Abundant' if i < temp else 'Deficient' if i > temp else 'Perfect')
