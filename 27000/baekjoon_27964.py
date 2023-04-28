input()
print('yummy' if sum(map(lambda x: x.endswith('Cheese'), set(input().split()))) > 3 else 'sad')
