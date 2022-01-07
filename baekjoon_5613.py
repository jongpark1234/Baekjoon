num = int(input())
while True:
    operator = input()
    if operator == '=':
        print(num)
        break
    temp = int(input())
    if operator == '+':
        num += temp
    elif operator == '-':
        num -= temp
    elif operator == '*':
        num *= temp
    else:
        num //= temp
