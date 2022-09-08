s = str(__import__('math').prod(int(input()) for _ in range(3)))
print(*[s.count(str(i)) for i in range(10)])
