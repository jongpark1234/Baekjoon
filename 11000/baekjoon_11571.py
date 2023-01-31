def solve(numerator, denominator):
    if numerator == 0:
        return '0.(0)'
    ret = []
    if (numerator > 0) != (denominator > 0):
        ret.append('-')
    numerator = abs(numerator)
    denominator = abs(denominator)
    ret.append(str(numerator // denominator))
    numerator %= denominator
    if numerator == 0:
        return "".join(ret)
    ret.append('.')
    dic = {}
    idx = len(ret)
    while numerator != 0:
        if numerator in dic:
            ret.insert(dic[numerator], '(')
            ret.append(')')
            return ''.join(ret)
        dic[numerator] = idx
        numerator *= 10
        ret.append(str(numerator // denominator))
        numerator %= denominator
        idx += 1
    return ''.join(ret)
for i in range(int(input())):
    a, b = map(int, input().split())
    result = solve(a, b)
    if '.' not in result:
        print(result + '.(0)')
    elif '(' not in result:
        print(result + '(0)')
    else:
        print(result)
