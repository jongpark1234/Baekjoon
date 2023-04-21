n = int(input())
variety = input().split()
m, k = map(int, input().split())
for _ in range(m):
    if list(map(lambda x: variety[x - 1], map(int, input().split()))) == ['W' for _ in range(k)]:
        print('W')
        break
else:
    print('P')
