SIZE = 256
PRINTABLECHARLIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255]
def stoi(i: str) -> int:
    return ord(i) - 48 if i.isdigit() else ord(i) - 87
def checkKeylen(numlist: list[int], keylen: int) -> bool:
    setlist = [set() for _ in range(keylen)]
    for i in range(len(numlist)):
        setlist[i % keylen].add(numlist[i])
    return keylen <= 2 or sum(map(lambda x: len(x), setlist)) // keylen < 40
def check(numlist: list[int], offset: int, key: int, keylen: int) -> bool:
    Sum = 0
    distribution = [0 for _ in range(SIZE)]
    for i in range(offset, len(numlist), keylen):
        distribution[numlist[i] ^ key] += 1
    for i in range(SIZE):
        if i in PRINTABLECHARLIST and distribution[i]:
            return False
        Sum += distribution[i]
    if distribution[32] < Sum // 15 or distribution[124] + distribution[126] > 20:
        return False
    if distribution[70] + distribution[102] + distribution[105] + distribution[115] + distribution[107] >= Sum * 0.5:
        return True
    uCase, lCase, space = sum(distribution[65:91]), sum(distribution[97:123]), distribution[32] + distribution[10]
    if uCase + lCase + space < Sum * 0.9 or uCase > lCase // 5:
        return False
    return sum(distribution[i] < lCase // 26 for i in [97, 101, 105, 116, 111]) < 2
def solve(numlist: list[int], keylen: int):
    if not checkKeylen(numlist, keylen):
        return
    passlist = [[] for _ in range(keylen)]
    key = [0 for _ in range(keylen)]
    for i in range(keylen):
        for j in range(SIZE - 1):
            if check(numlist, i, j, keylen):
                passlist[i].append(j)
        if not passlist[i]:
            return
    for i in range(keylen):
        key[i] = passlist[i][0]
    print(''.join(map(lambda x: chr(x), [numlist[i] ^ key[i % len(key)] for i in range(len(numlist))])).strip())
    exit()
numlist, encrypted = [], ''
for i in [*open(0)]:
    encrypted += i.strip()
for i in range(0, len(encrypted), 2):
    numlist.append(stoi(encrypted[i]) * 16 + stoi(encrypted[i + 1]))
for i in range(1, 11):
    solve(numlist, i)
