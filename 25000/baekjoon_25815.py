y, m = map(int, input().split())
print(*divmod(m * 15 if y < 1 else m * 9 + 180 if y < 2 else 288 + ((y - 2) * 12 + m) * 4, 12))
