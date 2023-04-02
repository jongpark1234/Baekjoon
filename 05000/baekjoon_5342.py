result = 0
costs = {
    'Paper': 57.99,
    'Printer': 120.50,
    'Planners': 31.25,
    'Binders': 22.50,
    'Calendar': 10.95,
    'Notebooks': 11.20,
    'Ink': 66.95
}
while (item := input()) != 'EOI':
    result += costs[item]
print(f'${result}')
