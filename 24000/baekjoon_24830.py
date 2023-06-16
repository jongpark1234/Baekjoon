prev = 1
for _ in range(int(input())):
    l, o, r = map(lambda x: int(x) if x.isnumeric() else x, input().split())
    if o == '+':
        prev = l + r - prev
    if o == '-':
        prev = (l - r) * prev
    if o == '*':
        prev = (l * r) ** 2
    if o == '/':
        prev = (l + l % 2) // 2
    print(prev)
