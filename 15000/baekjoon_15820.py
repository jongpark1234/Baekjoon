s1, s2 = map(int, input().split())
for i in range(s1):
    a, b = map(int, input().split())
    if a != b:
        print("Wrong Answer")
        exit()
for i in range(s2):
    a, b = map(int, input().split())
    if a != b:
        print("Why Wrong!!!")
        exit()
print('Accepted')
