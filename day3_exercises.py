my_age = int(30)
print(type(my_age))

my_height = float('68')
print(type(my_height))

complex_num = 4 + j
print(complex_num)

# Input function gives a directive to the user to present it the value which will be saved as an object
# Then with those variables set, you can create another variable like area which is a formula included those
base = input('what is the base of the trianlge?: ')
height = input('what is the height of the triangle?: ')
print(area := 0.5 * base * height)

a = input('What is the value of triangle side a?: ')
b = input('What is the value of triangle side b?: ')
c = input('What is the value of triangle side c:? ')
print(perimeter := a + b + c)

length = input('What is the length of the rectangle?: ')
width = input('What is the width of the rectangle?: ')
print(area := length * width)
print(perimeter := 2 * length * width)

import math
radius = input('What is the radius of the circle?: ')
print(area := math.pi * radius**2)
print(circumference := 2 * math.pi * radius)

# Don't appproach thinking 'how do i make python reason algebra'
# Instead think what quantities do i already know how to calculate and how do i express those calculation?
# y = 2x - 2
# y = mx + b
# m = slope
# x = x or where y = 0 in our slope intercept equation
# b = y-intercept
# The x-intercept is where y = 0 so  0 = 2x - 2 and x = 1
print('Slope:', slope_m := 2)
print('y-intercept:', y_int := -2)
print('x-intercept:', x_int := slope_m / y_int)
# Start with setting what you know than use those variables and other known relationships to calculate like by hand

# Slope is (m = y2-y1/x2-x1) and we need to find slope and Euclidean distance between (2,2) (6,10)

