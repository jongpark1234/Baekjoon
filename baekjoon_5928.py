d, h, m = map(int, input().split())
end = d * 1440 + h * 60 + m - 16511
print(end if end > -1 else -1)
