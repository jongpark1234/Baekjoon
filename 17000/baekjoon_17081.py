Map = []
monsters = []
chests = []
spiketraps = []
equipment = []
k = 0
l = 0 
turn = 0
Xpos, Ypos = 0, 0
level = 1
die = False
maxExp = level * 5
exp = 0
normalDamage = 2
weaponDamage = 0
Damage = normalDamage + weaponDamage
normalArmor = 2
suitArmor = 0
Armor = normalArmor + suitArmor
health = 20
maxHealth = 20
killTheBoss = False
accessory = []
n, m = map(int, input().split())
for i in range(n):
    a = input()
    k += a.count('&') + a.count('M')
    l += a.count('B')
    for j in range(m):
        if a[j] == '^':
            spiketraps.append([i, j])
    if '@' in a:
        Xpos, Ypos = a.index('@'), i
        FirstSpawnXpos, FirstSpawnYpos = Xpos, Ypos
        a = a.replace('@', '.')
    Map.append(list(a))
S = input()
for i in range(k):
    r, c, s, w, a, h, e = input().split()
    monsters.append([int(r) - 1, int(c) - 1, s, int(w), int(a), int(h), int(e)])
for i in range(l):
    r, c, t, s = input().split()
    chests.append([int(r) - 1, int(c) - 1, t, s])
for i in S:
    turn += 1
    if i == 'L':
        if Xpos != 0:
            if Map[Ypos][Xpos - 1] != '#':
                Xpos -= 1
    elif i == 'R':
        if Xpos != m - 1:
            if Map[Ypos][Xpos + 1] != '#':
                Xpos += 1
    elif i == 'U':
        if Ypos != 0:
            if Map[Ypos - 1][Xpos] != '#':
                Ypos -= 1
    elif i == 'D':
        if Ypos != n - 1:
            if Map[Ypos + 1][Xpos] != '#':
                Ypos += 1
    if Map[Ypos][Xpos] == 'B':
        Map[Ypos][Xpos] = '.'
        for chest in chests:
            if chest[:2] == [Ypos, Xpos]:
                if chest[2] == 'W':
                    weaponDamage = int(chest[3])
                elif chest[2] == 'A':
                    suitArmor = int(chest[3])
                else:
                    if len(accessory) != 4 and chest[3] not in accessory:
                        accessory.append(chest[3])
                break
    elif Map[Ypos][Xpos] == '^':
        MobName = 'SPIKE TRAP'
        if 'DX' in accessory:
            health -= 1
        else:
            health -= 5
    elif Map[Ypos][Xpos] == '&':
        for monster in monsters:
            if monster[:2] == [Ypos, Xpos]:
                mobInfo = monster[:]
                break
        MobName = mobInfo[2]
        MobDamage = mobInfo[3]
        MobArmor = mobInfo[4]
        MobHealth = mobInfo[5]
        MobExp = mobInfo[6]
        BattleTurn = 0
        while True:
            if BattleTurn == 0:
                if 'CO' in accessory and 'DX' in accessory:
                    MobHealth -= max(1, Damage * 3 - MobArmor)
                elif 'CO' in accessory:
                    MobHealth -= max(1, Damage * 2 - MobArmor)
                else:
                    MobHealth -= max(1, Damage - MobArmor)
            else:
                MobHealth -= max(1, Damage - MobArmor)
            if MobHealth <= 0:
                Map[Ypos][Xpos] = '.'
                if 'HR' in accessory:
                    health = min(maxHealth, health + 3)
                if 'EX' in accessory:
                    exp += int(MobExp * 1.2)
                else:
                    exp += MobExp
                break
            health -= max(1, MobDamage - Armor)
            if health <= 0:
                break
            BattleTurn += 1
    elif Map[Ypos][Xpos] == 'M':
        if 'HU' in accessory:
            health = maxHealth
        for monster in monsters:
            if monster[:2] == [Ypos, Xpos]:
                mobInfo = monster[:]
                break
        MobName = mobInfo[2]
        MobDamage = mobInfo[3]
        MobArmor = mobInfo[4]
        MobHealth = mobInfo[5]
        MobExp = mobInfo[6]
        BattleTurn = 0
        while True:
            if BattleTurn == 0:
                if 'CO' in accessory and 'DX' in accessory:
                    MobHealth -= max(1, Damage * 3 - MobArmor)
                elif 'CO' in accessory:
                    MobHealth -= max(1, Damage * 2 - MobArmor)
                else:
                    MobHealth -= max(1, Damage - MobArmor)
            else:
                MobHealth -= max(1, Damage - MobArmor)
            if MobHealth <= 0:
                killTheBoss = True
                Map[Ypos][Xpos] = '.'
                if 'HR' in accessory:
                    health = min(maxHealth, health + 3)
                if 'EX' in accessory:
                    exp += int(MobExp * 1.2)
                else:
                    exp += MobExp
                break
            if BattleTurn == 0 and 'HU' in accessory:
                health -= 0
            else:
                health -= max(1, MobDamage - Armor)
            if health <= 0:
                break
            BattleTurn += 1
    if health <= 0:
        health = 0
        if 'RE' in accessory:
            health = maxHealth
            Xpos, Ypos = FirstSpawnXpos, FirstSpawnYpos
            accessory.remove('RE')
        else:
            die = True
            break
    if exp >= maxExp:
        level += 1
        exp = 0
        maxExp = 5 * level
        maxHealth += 5
        health = maxHealth
        normalDamage += 2
        normalArmor += 2
    if killTheBoss:
        break
    Damage = normalDamage + weaponDamage
    Armor = normalArmor + suitArmor
for i in range(n):
    for j in range(m):
        if [i, j] == [Ypos, Xpos] and not die:
            print('@', end = '')
        else:
            print(Map[i][j], end = '')
    print()
print(f'Passed Turns : {turn}')
print(f'LV : {level}')
print(f'HP : {health}/{maxHealth}')
print(f'ATT : {normalDamage}+{weaponDamage}')
print(f'DEF : {normalArmor}+{suitArmor}')
print(f'EXP : {exp}/{maxExp}')
if killTheBoss:
    print('YOU WIN!')
elif die:
    print(f'YOU HAVE BEEN KILLED BY {MobName}..')
else:
    print('Press any key to continue.')        
