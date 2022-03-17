line = 0
while True:
    try:
        input()
        line += 1
    except EOFError:
        break
print(line)
