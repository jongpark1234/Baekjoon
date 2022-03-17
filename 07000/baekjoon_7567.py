dishes = list(map(str, input()))
previous = '0'
height = 0
for i in range(len(dishes)):
    if dishes[i] == previous:
        height += 5
    else:
        height += 10
    previous = dishes[i]
print(height)
