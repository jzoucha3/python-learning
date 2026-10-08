# 1) Create an empty dictionary called dog
dog = {}
print(dog)

# 2) Add name, color, breed, legs, age to the dog dictionary
dog['name', 'color', 'breed', 'legs', 'age'] = ['pogi', 'black and brown', 'rottie', 4, 3]
print(dog)

# 3) Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name' : 'james',
           'last_name' : 'zoucha',
           'gender' : 'male',
           'age' : 30,
           'marital status' : 'smitten',
           'skills' : 'likes working',
           'country' : 'US',
           'city' : 'Denver',
           }
print(student)

# 4) Get the length of the student dictionary
print(len(student))

# 5) Get the value of skills and check the data type, it should be a list
print(student.get('skills'))
print(type(student['skills']))

# 6) Modify the skills values by adding one or two skills
student['skills'] = ['likes working']
student['skills'].extend(['self-motivating', 'empowers others'])
print(student['skills'])

# 7) Get the dictionary keys as a list
print(student.keys())

# 8) Get the dictionary values as a list
print(student.values)

# 9) Change the dictionary to a list of tuples using items() method
stuples = student.items()
print(stuples)

# 10) Delete one of the items in the dictionary
student.pop('skills')
print(student)

# 11) Delete one of the dictionaries
del student