for _ in range(int(input())):
    steps = input()
    print(len(steps[:steps.index('D')]) if steps.find('D') != -1 else len(steps))
