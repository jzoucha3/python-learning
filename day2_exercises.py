# Day 2: 30 Days pf python programming

first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on = 'james', 'zoucha', 'james zoucha', 'US', 'Greeley', 30, 2026, 'no', 'True', 'no'

print(first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on)

variables = [
    first_name,
    last_name,
    full_name,
    country,
    city,
    age,
    year,
    is_married,
    is_true,
    is_light_on
]

for variable in variables:
    print(type(variable))

print(len(first_name))

num_one = 5
print(num_one)

num_two = 4
print(num_two)

add_one_two = num_one + num_two
print(add_one_two)

print(diff_one_two := num_one - num_two)

print(prod_one_two := num_one * num_two)

print(div_one_two := num_one / num_two)

print(mod_one_two := num_two % num_one)

print(power_one_two := num_one**num_two)

print(floor_one_two := num_one // num_two)

import math
circle_r = 30
print(area := 2*math.pi*circle_r**2)
print(circum := 2*math.pi*circle_r)

radius = float(input("Enter radius: "))
area = math.pi * radius ** 2
print(area)

