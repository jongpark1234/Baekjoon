def process(numlist: list[int]) -> int:
    ret = maxValue = 0
    for i in numlist:
        if i > maxValue:
            maxValue = i
            ret += 1
    return ret
trophies = [int(input()) for _ in range(int(input()))]
print(process(trophies), process(trophies[::-1]))
