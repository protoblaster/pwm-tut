#birth_year = input('Birth Year: ')
#age = 2019 - birth_year             # error occurs here
#print(age)

birth_year = int(input('Birth Year: '))
age = 2019 - birth_year
print(age)

birth_year = input('Birth Year: ')
age = 2019 - int(birth_year)
print(age)

print(type(birth_year))             # prints type of var
print(type(age))                    # prints type of var