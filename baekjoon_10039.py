temp = 0
for i in range(5):
    n = int(input())
    if n < 40:
        n = 40
    temp += n
print(int(temp / 5))
