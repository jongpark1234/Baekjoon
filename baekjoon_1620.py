import sys
n, m = map(int, sys.stdin.readline().split())
pokemon_list = []
pokemon_dict = {}
for i in range(n):
    pk = sys.stdin.readline().rstrip()
    pokemon_list.append(pk)
    pokemon_dict[pk] = i + 1
for _ in range(m):
    keyword = sys.stdin.readline().rstrip()
    try:
        temp = int(keyword)
    except:
        print(pokemon_dict[keyword])
    else:
        print(pokemon_list[temp - 1])
