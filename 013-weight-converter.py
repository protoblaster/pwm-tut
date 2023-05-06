weight = float(input('Weight: '))
unit = input('(L)bs or (K)g: ')

if unit.upper() == 'L':
    kg = weight * 0.45
    print(f'You are {kg} Kilos.')
else:
    lbs = weight / 0.45
    print(f'You are {lbs} Pounds')