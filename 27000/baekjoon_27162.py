def ones(numlist: list[int]) -> int:
    return numlist.count(1) * 1
def twos(numlist: list[int]) -> int:
    return numlist.count(2) * 2
def threes(numlist: list[int]) -> int:
    return numlist.count(3) * 3
def fours(numlist: list[int]) -> int:
    return numlist.count(4) * 4
def fives(numlist: list[int]) -> int:
    return numlist.count(5) * 5
def sixes(numlist: list[int]) -> int:
    return numlist.count(6) * 6
def fourOfAKind(numlist: list[int]) -> int:
    for i in range(1, 7):
        if numlist.count(i) >= 4:
            return i * 4
    return 0
def fullHouse(numlist: list[int]) -> int:
    two = three = False
    if len(set(numlist)) == 2:
        for i in set(numlist):
            if numlist.count(i) == 3:
                three = True
            elif numlist.count(i) == 2:
                two = True
    return sum(numlist) if two and three else 0
def littleStraight(numlist: list[int]) -> int:
    return 30 if sorted(numlist) == [1, 2, 3, 4, 5] else 0
def bigStraight(numlist: list[int]) -> int:
    return 30 if sorted(numlist) == [2, 3, 4, 5, 6] else 0
def yacht(numlist: list[int]) -> int:
    return 50 if len(set(numlist)) == 1 else 0
def choice(numlist: list[int]) -> int:
    return sum(numlist)
results = [0]
genealogy = input()
fixed = list(map(int, input().split()))
for i in range(1, 7):
    for j in range(1, 7):
        for k in range(12):
            if genealogy[k] == 'N':
                continue
            if k == 0:
                results.append(ones(fixed + [i, j]))
            elif k == 1:
                results.append(twos(fixed + [i, j]))
            elif k == 2:
                results.append(threes(fixed + [i, j]))
            elif k == 3:
                results.append(fours(fixed + [i, j]))
            elif k == 4:
                results.append(fives(fixed + [i, j]))
            elif k == 5:
                results.append(sixes(fixed + [i, j]))
            elif k == 6:
                results.append(fourOfAKind(fixed + [i, j]))
            elif k == 7:
                results.append(fullHouse(fixed + [i, j]))
            elif k == 8:
                results.append(littleStraight(fixed + [i, j]))
            elif k == 9:
                results.append(bigStraight(fixed + [i, j]))
            elif k == 10:
                results.append(yacht(fixed + [i, j]))
            elif k == 11:
                results.append(choice(fixed + [i, j]))
print(max(results))
