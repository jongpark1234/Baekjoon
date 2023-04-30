n = int(input())
result = cat = 0
while cat < n:
    result += 1
    cat = min(n, cat + 1 if cat < 2 else cat << 1)
print(result)
