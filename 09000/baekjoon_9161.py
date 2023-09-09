for mole in range(100, 1000):
    for deno in range(100, 1000):
        if str(mole)[-1] == str(deno)[0]:
            cMole = int(str(mole)[:-1])
            cDeno = int(str(deno)[1:])
            if cDeno != 0:
                if len(set(str(mole))) == len(set(str(deno))) == 1:
                    continue
                if cMole / cDeno == mole / deno:
                    print(f'{mole} / {deno} = {cMole} / {cDeno}')
