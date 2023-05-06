course = "Python's course for beginners"
print(course)

course1 = 'Python course for "Beginners'
print(course)

print('Length of "course" string:', len(course))
print('Index position 8:', course[9])

for i in range(6):
    print(course[i], end='')        # print first 6 index's
    print(' ')

for i in range(6):
    print(course[-i], end='')       # print backwards last 6 index's
    print(' ')

# create a string using index's
message = course[0:4]      # doesn't return 3rd index
print(message)

print(course[0:])          # print all index's from 0

# step (print every nth letter)
print(course[::2])         # where n = 3nd letter (2nd index)

course1 = course[:]        # returns all characters in course variable
print(course1)