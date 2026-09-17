# Variables and Built In Functions

# Built Ins
- Built in functions are native to python once installed and can be applied to data singularly or in combination with others

# Variables
- Variables store data in computer memory
- It is best to use easy naming convention (mnemonic)
- Naming rules include
1) A variable name must start with a letter or the underscore character
2) A variable name cannot start with a number
3) A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
4) Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)

# Variables in Python
`
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }
`

`
print('Hello, World!') # The text Hello, World! is an argument
print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # it takes only one argument
`

# Printing the values stored in the variables
`
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)
`

# Multiple at Once
`
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
`

# Input Funciton
`
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)
`

# Different python data types
# Let's declare variables with various data types
`
first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int, it is not my real age, don't worry about it
`

# Printing out types
`
print(type('Asabeneh'))          # str
print(type(first_name))          # str
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3, 4]))        # list
print(type({'name':'Asabeneh'})) # dict
print(type((1,2)))               # tuple
print(type(zip([1,2],[3,4])))    # zip
`

# int to float
`
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0
`

# float to int
`
gravity = 9.81
print(int(gravity))             # 9
`

# int to str
`
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'
`

# str to int or float
`
num_str = '10.6'
num_float = float(num_str)  # Convert the string to a float first
num_int = int(num_float)    # Then convert the float to an integer
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10
`

# str to list
`
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
`

# Exercises
Level 1
1) Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
2) Write a python comment saying 'Day 2: 30 Days of python programming'
3) Declare a first name variable and assign a value to it
4) Declare a last name variable and assign a value to it
5) Declare a full name variable and assign a value to it
6) Declare a country variable and assign a value to it
7) Declare a city variable and assign a value to it
8) Declare an age variable and assign a value to it
9) Declare a year variable and assign a value to it
10) Declare a variable is_married and assign a value to it
11) Declare a variable is_true and assign a value to it
12) Declare a variable is_light_on and assign a value to it
13) Declare multiple variable on one line

Level 2
1) Check the data type of all your variables using type() built-in function
2) Using the len() built-in function, find the length of your first name
3) Compare the length of your first name and your last name
4) Declare 5 as num_one and 4 as num_two
5) Add num_one and num_two and assign the value to a variable total
6) Subtract num_two from num_one and assign the value to a variable diff
7) Multiply num_two and num_one and assign the value to a variable product
8) Divide num_one by num_two and assign the value to a variable division
9) Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
10) Calculate num_one to the power of num_two and assign the value to a variable exp
11) Find floor division of num_one by num_two and assign the value to a variable floor_division
12) The radius of a circle is 30 meters.
- Calculate the area of a circle and assign the value to a variable name of area_of_circle
- Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
- Take radius as user input and calculate the area.
13) Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
14) Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
