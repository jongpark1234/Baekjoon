result = ['..........' for _ in range(10)]
for i in range(10):
    Input = list(map(int, input().split()))
    for j in range(10):
        if Input[j] == 100:
            r, c = i, j
if c & 1:
    result[r % 10] = '####.###.#'
    result[(r + 2) % 10] = '###.#.#.##'
    result[(r + 4) % 10] = '##.##.#...'
else:
    result[r % 10] = '###.#.#.##'
    result[(r + 2) % 10] = '####.###.#'
    result[(r + 4) % 10] = '##.##.#...'
print('\n'.join(result))
