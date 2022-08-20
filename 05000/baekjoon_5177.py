for i in range(int(input())):
    s1 = ' '.join(input().strip().lower().split()).replace('{', '(').replace('[', '(').replace(']', ')').replace('}', ')').replace(';', ',').replace(' (', '(').replace('( ', '(').replace(' )', ')').replace(') ', ')').replace(' .', '.').replace('. ', '.').replace(' ,', ',').replace(', ', ',').replace(' :', ':').replace(': ', ':')
    s2 = ' '.join(input().strip().lower().split()).replace('{', '(').replace('[', '(').replace(']', ')').replace('}', ')').replace(';', ',').replace(' (', '(').replace('( ', '(').replace(' )', ')').replace(') ', ')').replace(' .', '.').replace('. ', '.').replace(' ,', ',').replace(', ', ',').replace(' :', ':').replace(': ', ':')
    print(f'Data Set {i + 1}:', 'equal' if s1 == s2 else 'not equal', end = '\n\n')
