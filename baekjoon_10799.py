previous = ''
stack, piece = 0, 0
ironbar = input()
for i in range(len(ironbar) - 1):
    if ironbar[i] == '(':
        if ironbar[i + 1] == '(':
            stack += 1
            piece += 1
        else:
            piece += stack
    else:
        if ironbar[i + 1] == '(':
            pass
        else:
            stack -= 1
print(piece)
