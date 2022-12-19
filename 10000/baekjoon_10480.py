for i in [*open(0)][1:]:
    print(f'{i.rstrip()} is {"odd" if int(i) & 1 else "even"}')
