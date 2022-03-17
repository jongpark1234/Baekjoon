s = input()
s = s.replace('::', ':^:')
ip = s.split(':')
for i in range(len(ip)):
    if ip[i] != '^':
        ip[i] = ip[i].zfill(4)
if '^' in ip:
    for i in range(9 - len(ip)):
        ip.insert(ip.index('^'), '0000')
    ip.remove('^')
print(':'.join(ip))
