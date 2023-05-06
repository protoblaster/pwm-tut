course = 'Python for beginners'

print('Length:', len(course))      # length of 'course'

print('Uppercase:', course.upper())   # convert 'course' to uppercase
print('Lowercase:', course.lower())   # convert 'course' to lowercase

print('Original Value:', course)           # 'course' is not modified

print('Beginners is at index:', course.find('beginners'))

print('Replace beginner with "absolute beginners":', course.replace('beginners', 'absolute beginners'))

# Boolean Expression
print('Python in "course":', 'Python' in course)
print('python in "course":', 'python' in course)