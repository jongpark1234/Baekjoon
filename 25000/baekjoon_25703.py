n = int(input())
space = ''
print('int a;')
for i in range(1, n + 1):
    print(f'int {"*" * i}ptr{space if i == 1 else i} = &{"a" if i == 1 else f"ptr{space if i - 1 == 1 else i - 1}"};')
