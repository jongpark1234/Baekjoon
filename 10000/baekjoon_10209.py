dir = 'urdl'
for i in range(int(input())):
    stack = []
    s = input()
    for j in s:
        if stack and stack[-1] == dir[(dir.index(j) + 2) % 4]:
            stack.pop()
        else:
            stack.append(j)
    print(f'Data Set {i + 1}:')
    print(['Yes', 'No'][bool(stack)], end='\n\n')
