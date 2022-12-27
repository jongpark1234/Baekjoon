from collections import deque
def get(numlist: deque[int]) -> int:
    ret = []
    for _ in range(4):
        numlist.append(numlist.popleft())
        ret.append(int(''.join(map(str, numlist))))
    return min(ret)
print(sum('0' not in str(i) and i == get(deque(list(map(int, str(i))))) for i in range(1111, get(deque(list(map(int, input().split())))))) + 1)
