numbers = [2, 2, 2, 2, 5]
symbols = 'x'

for symbol_count in numbers:
    output = ''
    for count in range(symbol_count):
        output += 'x'
    print(output)