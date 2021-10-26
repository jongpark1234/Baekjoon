al = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
string = input()
for i in al:
    string = string.replace(i, '*')
print(len(string))
