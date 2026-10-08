# 💻 Exercises: Day 10
# Exercises: Level 1

# 1) Iterate 0 to 10 using for loop, do the same using while loop.
numbers = range(1, 11, 1)

for number in numbers:
    print(number)

# 2) Iterate 10 to 0 using for loop, do the same using while loop.
numbers = range(10,-1, -1)

for number in numbers:
    print(number)

while number > 0:
    print(number)


# 3) Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######
prints = range(1, 8)

for i in prints:
    print('#' * i)


# 4) Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

height = 8
width = 8

for i in range(height):
    for j in range(width):
        print('#', end=' ')
    print()

# 5) Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

numbers = range(0,11,1)

for i in numbers:
    print(f'{i} * {i} = {i * i} ')


# 6) Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] 
# using a for loop and print out the items.
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']

for i in lst:
    print(i)

# 7) Use for loop to iterate from 0 to 100 and print only even numbers
numbers = range(1,101,1)

for i in numbers:
    if i % 2 == 0:
        print(i)

# 8) Use for loop to iterate from 0 to 100 and print only odd numbers
numbers = range(1,101,1)

for i in numbers:
    if i % 2 != 0:
        print(i)


# Exercises: Level 2

# 9) Use for loop to iterate from 0 to 100 and print the sum of all numbers.
numbers = range(1,101)
total = 0

for i in numbers:
    total = total + i

print(total)


# 10) Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
numbers = range(1,101)
total_even = 0
total_odd = 0

for i in numbers:
    if i % 2 == 0:
        total_even = total_even + i
    else:
        total_odd = total_odd + i

print(total_even)
print(total_odd)

# another way to shorten since same operation is applied...
total = [0,0]

for i in numbers:
    total[i % 2] += i

print(total)

# Exercises: Level 3

# 11) Go to the data folder and use the countries.py file. 
# Loop through the countries and extract all the countries containing the word land.
from data.countries import countries

lands = []

for country in countries:
    if 'land' in country:
        lands.append(country)

print(lands)

# 12) This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for fruit in fruits:
    reversed_fruits.insert(0, fruit)

print(reversed_fruits)

# second approach to modify ordering but save back into same
# avoids iterating over list while simultaneously moving elements around

fruits = ['banana', 'orange', 'mango', 'lemon']

for i in range(len(fruits) // 2):
    fruits[i], fruits[-(i + 1)] = fruits[-(i + 1)], fruits[i]

print(fruits)

# Go to the data folder and use the countries-data.py file.
# 14) What are the total number of languages in the data
from data.countries_data import countries_data

unique_langauges = set()

for country in countries_data:
    languages = country['languages']
    
    for language in languages:
        unique_langauges.add(language)

print(len(unique_langauges))


# 15) Find the ten most spoken languages from the data
from data.countries_data import countries_data

languages_count = {}

for country in countries_data:
    languages = country['languages']
    
    for language in languages:
        if language in languages_count:
            languages_count[language] += 1
        else:
            languages_count[language] = 1

sort_languages = sorted(
    languages_count.items(),
    key=lambda x: x[1],
    reverse = True
)

for languages, count in sort_languages[:10]:
    print(languages, count)


# 16) Find the 10 most populated countries in the world
from data.countries_data import countries_data

population_count = {}

for country in countries_data:
    name = country['name']
    population = country['population']

    population_count[name] = population

sort_populations = sorted(
    population_count.items(),
    key=lambda x: x[1],
    reverse=True
)

for country, population in sort_populations[:10]:
    print(country, population)
