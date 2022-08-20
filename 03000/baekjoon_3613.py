variable = input()
def erring():
    print('Error!')
    exit(0)
if '__' in variable:
    erring()
if variable[0] == '_' or variable[-1] == '_':
    erring()
if '_' in variable:
    if variable.lower() != variable:
        erring()
    variable = variable.split('_')
    print(variable[0], end = '')
    for i in variable[1:]:
        print(i.capitalize(), end = '')
else:
    if variable[0].isupper():
        erring()
    for i in variable:
        print('_' + i.lower() if i.isupper() else i, end = '')
