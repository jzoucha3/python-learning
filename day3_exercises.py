age = 30
print("Age:", age)


height = 5.8
print("Height:", height)


complex_number = 2 + 3j
print("Complex number:", complex_number)


base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print("The area of the triangle is:", area)


side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is:", perimeter)


length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))
area = length * width
perimeter = 2 * (length + width)
print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)


radius = float(input("Enter radius: "))
pi = 3.14
area = pi * radius * radius
circumference = 2 * pi * radius
print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)


slope = 2
y_intercept = -2
x_intercept = -y_intercept / slope
print("The slope is:", slope)
print("The x-intercept is:", x_intercept)
print("The y-intercept is:", y_intercept)


x = [2, 6]
y = [2, 10]
slope = (y[1] - y[0]) / (x[1] - x[0])
distance = ((x[1] - x[0]) ** 2 + (y[1] - y[0]) ** 2) ** 0.5
print("The slope is:", slope)
print("The Euclidean distance is:", distance)


slope_task_8 = 2
slope_task_9 = (10 - 2) / (6 - 2)
print("The slopes are equal:", slope_task_8 == slope_task_9)


x = float(input("Enter a value for x: "))
y = x ** 2 + 6 * x + 9
print("The value of y is:", y)
print("Is y equal to zero?", y == 0)


python_length = len("python")
dragon_length = len("dragon")
print("The length of python is:", python_length)
print("The length of dragon is:", dragon_length)
print("Python is longer than dragon:", python_length > dragon_length)


result = "on" in "python" and "on" in "dragon"
print("'on' is in both python and dragon:", result)


sentence = "I hope this course is not full of jargon"
result = "jargon" in sentence
print("'jargon' is in the sentence:", result)


result = not ("on" in "dragon" and "on" in "python")
print("'on' is not in both dragon and python:", result)


python_length = len("python")
length_float = float(python_length)
length_string = str(length_float)
print("Length of python:", python_length)
print("Length converted to float:", length_float)
print("Float converted to string:", length_string)


number = int(input("Enter a number: "))
is_even = number % 2 == 0
print("The number is even:", is_even)


floor_result = 7 // 3
integer_result = int(2.7)
print("7 // 3 is equal to int(2.7):", floor_result == integer_result)


result = type("10") == type(10)
print("The types of '10' and 10 are equal:", result)


try:
    result = int("9.8") == 10
    print("int('9.8') is equal to 10:", result)
except ValueError as error:
    print("Error converting '9.8' to an integer:", error)
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
pay = hours * rate
print("Your weekly earning is:", pay)


years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds.")


table = [
    [1, 1, 1, 1, 1],
    [2, 1, 2, 4, 8],
    [3, 1, 3, 9, 27],
    [4, 1, 4, 16, 64],
    [5, 1, 5, 25, 125]
]

print("The table is:")
print(*table[0])
print(*table[1])
print(*table[2])
print(*table[3])
print(*table[4])
