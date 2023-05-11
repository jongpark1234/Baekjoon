result = 0
s = input()
while True:
    try:
        result += input().count(s)
    except EOFError:
        break
print(result)
