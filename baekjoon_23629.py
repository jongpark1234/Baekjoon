import re
def madness():
    print('Madness!')
    exit(0)
num = [['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']]
operator = []
result = []
s = input()
if not all(i in "EFGHINORSTUVWXZ+-x/=" for i in s):
    madness()
for i in range(10):
    s = s.replace(num[0][i], num[1][i])
result.append(s)
s = s.replace('=', '')
for i in s:
    if i == '+' or i == '-':
        operator.append(i)
    elif i == 'x':
        operator.append('*')
    elif i == '/':
        operator.append('//')
s = re.split(r'[-,+,x,/]', s)
temp = s[0]
for i in range(len(operator)):
    try:
        if operator[i] == '//':
            if int(temp) < 0:
                temp = str(-(abs(int(temp)) // int(s[i + 1])))
            else:
                temp = str(int(temp) // int(s[i + 1]))
        else:
            temp = str(eval(temp + operator[i] + s[i + 1]))
    except:
        madness()
for i in range(10):
    temp = temp.replace(num[1][i], num[0][i])
result.append(temp)
print('\n'.join(result))
