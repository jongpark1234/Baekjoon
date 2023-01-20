for i in [*open(0)]:
    print(i.strip().replace('i', '#').replace('e', 'i').replace('#', 'e').replace('I', '#').replace('E', 'I').replace('#', 'E'))
