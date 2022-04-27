birth = {}
death = {}
mother = {}
father = {}
descendant = {}
def ANCESTORS(name, space):
    parents = []
    if name in mother.keys():
        parents.append(mother[name])
    if name in father.keys():
        parents.append(father[name])
    parents.sort()
    if len(parents) == 0:
        return
    BIRTH = birth.keys()
    DEATH = death.keys()
    for i in parents:
        print(' ' * space, end = '')
        if i in BIRTH and i in DEATH:
            print(f'{i} {birth[i]} - {death[i]}')
        elif i in BIRTH:
            print(f'{i} {birth[i]} -')
        elif i in DEATH:
            print(f'{i} - {death[i]}')
        else:
            print(f'{i}')
        ANCESTORS(i, space + 2)
def DESCENDANTS(name, space):
    if name not in descendant.keys():
        return
    des = descendant[name]
    des.sort()
    BIRTH = birth.keys()
    DEATH = death.keys()
    for i in des:
        print(' ' * space, end = '')
        if i in BIRTH and i in DEATH:
            print(f'{i} {birth[i]} - {death[i]}')
        elif i in BIRTH:
            print(f'{i} {birth[i]} -')
        elif i in DEATH:
            print(f'{i} - {death[i]}')
        else:
            print(f'{i}')
        DESCENDANTS(i, space + 2)
while True:
    cmd = input()
    if cmd == 'QUIT':
        break
    if cmd.split()[0] == 'BIRTH':
        cmd = cmd[6:].split(':')
        for i in range(4):
            cmd[i] = cmd[i].strip()
        birth[cmd[0]] = cmd[1]
        mother[cmd[0]] = cmd[2]
        father[cmd[0]] = cmd[3]
        for i in range(2):
            if cmd[i + 2] not in descendant.keys():
                descendant[cmd[i + 2]] = []
            descendant[cmd[i + 2]].append(cmd[0])
    elif cmd.split()[0] == 'DEATH':
        cmd = cmd[6:].split(':')
        for i in range(2):
            cmd[i] = cmd[i].strip()
        death[cmd[0]] = cmd[1]
    elif cmd.split()[0] == 'ANCESTORS':
        name = cmd[10:]
        print(f'ANCESTORS of {name}')
        ANCESTORS(name, 2)
        print()
    elif cmd.split()[0] == 'DESCENDANTS':
        name = cmd[12:]
        print(f'DESCENDANTS of {name}')
        DESCENDANTS(name, 2)
        print()
