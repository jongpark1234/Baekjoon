period = [[-1 for _ in range(2097153)] for _ in range(21)]
def calc(gurdurr, length):
    if period[length][gurdurr] != -1:
        return period[length][gurdurr]
    next = [False for _ in range(20)]
    for i in range(length):
        if (gurdurr >> i) & 1:
            x = y = 0
            gurdurr ^= 1 << i
            next[calc(gurdurr, length)] = True
            for j in range(i):
                x |= (gurdurr >> j) & 1
                x <<= 1
            x >>= 1
            for j in range(length - i - 1):
                y |= (gurdurr >> (i + j + 1)) & 1
                y <<= 1
            y >>= 1
            next[calc(x, i) ^ calc(y, length - i - 1)] = True
            gurdurr ^= 1 << i
        else:
            temp = x = y = 0
            if i > 0:
                temp ^= (gurdurr >> (i - 1)) & 1
                for j in range(i - 1):
                    x |= (gurdurr >> j) & 1
                    x <<= 1
                x >>= 1
                temp ^= calc(x, i - 1)
            if i < length - 1:
                temp ^= (gurdurr >> (i + 1)) & 1
                for j in range(length- i - 2):
                    y |= (gurdurr >> (i + j + 2)) & 1
                    y <<= 1
                y >>= 1
                temp ^= calc(y, length- i - 2)
            next[temp] = True
    for i in range(20):
        if not next[i]:
            period[length][gurdurr] = i
            return i
def solve(gurdurr):
    ret, value, seg = 0, 1, []
    for i in range(1, len(gurdurr)- 1):
        if gurdurr[i] == '2':
            gurdurr[i] = '0'
        elif gurdurr[i] == '1':
            ret ^= (gurdurr[i - 1] == '4') ^ (gurdurr[i + 1] == '4')
            gurdurr[i - 1] = gurdurr[i] = gurdurr[i + 1] = '0'
    for i in range(1, len(gurdurr)):
        if gurdurr[i] == '0':
            if value != i:
                seg.append([value, i - 1])
            value = i + 1
    for i in seg:
        temp = 0
        for j in gurdurr[i[0]:i[1] + 1]:
            temp |= j == '4'
            temp <<= 1
        temp >>= 1
        ret ^= calc(temp, i[1] - i[0] + 1)
    return ret
for _ in range(int(input())):
    result = ['0']
    for _ in range(int(input())):
        s = input()
        result.append('1' if s == '.I.' else '2' if s == 'I.I' else '3' if s == 'II.' or s == '.II' else '4')
    print('First' if solve(result + ['0']) else 'Second')
