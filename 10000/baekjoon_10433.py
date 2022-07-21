def solve(gould: int) -> int:
    sign = gould & 2147483648
    expc = (gould & 2130706432) >> 24
    expv = expc - 64
    mantissa = gould & 16777215
    if mantissa == 0:
        return 0
    expv <<= 2
    while (mantissa & 8388608) == 0:
        mantissa <<= 1
        expv -= 1
    expv -= 1
    if expv > 127:
        ret = sign | 2139095040
    elif expv < -149:
        ret = sign
    elif expv > -127:
        expc = expv + 127
        expc <<= 23
        ret = sign | expc | (mantissa & 8388607)
    else:
        while expv < -126:
            expv += 1
            mantissa >>= 1
        expc = 0
        ret = sign | expc | (mantissa & 8388607)
    return ret
for i in range(int(input())):
    idx, gould = input().split()
    print(i + 1, hex(solve(int(gould, 16)))[2:].upper().zfill(8))
