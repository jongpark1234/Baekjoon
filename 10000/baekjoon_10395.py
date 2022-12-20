numlists = [list(map(int, input().split())) for _ in range(2)]
for i in range(5):
    if not numlists[0][i] ^ numlists[1][i]:
        print('N')
        break
else:
    print('Y')
