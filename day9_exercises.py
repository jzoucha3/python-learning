# Exercises: Level 1
# 1) Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
age = int(input('Enter your age: '))
if age >= 18:
    print('you are old enough to drive')
else:
    print(f'you need {18 - age} more years to learn to drive')




# 2) Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? 
# Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in 
# age, 'years' for bigger differences, and a custom text if my_age = your_age. 
# Output:
# Enter your age: 30
# You are 5 years older than me.
age = int(input('Enter your age: '))
your_age = age
my_age = 43

if your_age > my_age:
    if abs(my_age - your_age) == 1:
        print('You are a year older than me')
    else:     
        print(f'You are {abs(my_age - your_age)} older than me')

elif your_age < my_age:
    if abs(my_age - your_age) == 1:
        print(f'I am a year older than you')
    else:
        print(f'I am {abs(my_age - your_age)} older than you')

else:
    print('We are the same age')


# 3) Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, else a is equal to b. 
# Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
a = input('What is the value of a: ')
b = input('What is the value of b: ')
if a < b:
    print('a is smaller than b')
elif a > b:
    print('a is larger than b')
else:
    print('a and b are the same')


# Exercises: Level 2
# 1) Write a code which gives grade to students according to theirs scores:
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
grade = int(input('What was your score: '))
if 0 <= abs(grade) <= 59:
    print('F')
elif 60 <= abs(grade) <= 69:
    print('D')
elif 70 <= grade <= 79:
    print('C')
elif 80 <= grade <= 89:
    print('B')
elif 90 <= grade <= 100:
    print('A')
else:
    print('check score again')

# 2) Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: 
# September, October or November, the season is Autumn. 
# December, January or February, the season is Winter. 
# March, April or May, the season is Spring 
# June, July or August, the season is Summer
month = str(input('What month is it: ').strip().lower())
if month == {'september', 'october', 'november'}:
    print('The season is Autum')
elif month == {'december', 'january', 'feburary'}:
    print('The season is winter')
elif month == {'march', 'april', 'may'}:
    print('The season is spring')
elif month == {'june', 'july', 'august'}:
    print('The season is summer')
else:
    print('Type in a true month spelled using English')

# 3) The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')
fruit = input('Type a fruit: ').strip().lower()
if fruit in fruits:
    print('That fruit already exists in the list')
else:
    fruits.append(fruit)
    print(fruits)

# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
# 1) Check if the person dictionary has skills key, 
# if so print out the middle skill in the skills list.
if 'skills' in person:
    middle = len(person['skills']) // 2

    if len(person['skills']) % 2 == 0:
        print([person['skills'][middle], person['skills'][middle - 1]])
    else:
        print((person['skills'][middle]))
else:
    print('No skills')

# 2) Check if the person dictionary has skills key, 
# if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    if 'python' in person['skills']:
        print(True)
    else:
        print(False)
else:
    print('No skills')

# 3) If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions can be nested!
if 'skills' in person:
    skills = set(person['skills'])

    fed = {'Javascript', 'React'}
    bed = {'Node', 'Python', 'MongoDB'}
    fsd = {'React', 'Node', 'MongoDB'}

    if fed.issubset(skills):
        print('They are a frontend developer')
    elif bed.issubset(skills):
        print('They are a backend developer')
    elif fsd.issubset(skills):
            print('They are a full stack developer')
    else:
        print('unknown title')
else:
    print('No skills')


# 4) If the person is married and if he lives in Finland, 
# print the information in the following format:
# Asabeneh Yetayeh lives in Finland. He is married.
# Assume you have looked up the keys, know it's one person and 
# datatypes already so you don't need to look up input patterns
if 'is_married' in person and 'country' in person:
    if True == person['is_married'] and 'Finland' in person['country']:
        print(f'{person['first_name'][0]} lives in Finland. He is married')
    else:
        print(f'We know {person['first_name'][0]} is either not married or not in Finland')
else:
    print('We do not have that information')
