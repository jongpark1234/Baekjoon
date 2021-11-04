n = int(input())
tf = ['NE', 'DA']
a, b = input().split('*')
for i in range(n):
    s = input()
    print(tf[s[:len(a)] == a and s[-len(b):] == b and len(''.join(a + b)) <= len(s)])
