def convert(n: int, base: int) -> str:
    from collections import deque
    ret = deque([])
    while n > 0:
        n, m = divmod(n, base)
        ret.appendleft(m)
    return ''.join(map(str, ret))
n, k = map(int, input().split())
print(convert(sum(map(int, map(lambda x: '0' if x == '' else x, convert(n, k).split('0')))), k))
