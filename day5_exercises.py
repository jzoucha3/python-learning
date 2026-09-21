# 1) Declare an empty list
print(empty_list := [])

# 2) Declare a list with more than 5 items
print(five_list := [1-5])

# 3) Find the length of your list
print(len(five_list))

# 4) Get the first item, the middle item and the last item of the list
(print(five_list[0:
                (middle := len(five_list)//2): 
                (last := int(len(five_list)))]))

# 5&7) Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
print(mixed_data := ['james', 30, 68, 'relationship', 'p.sherman'])

# 6&7) Declare a list variable named it_companies and assign initial values 
# Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
print(it_companies := ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'])

# 8) Print the number of companies in the list
print(it_companies)
print(len(it_companies))

# 9) Print the first, middle and last company
print(it_companies)
print(it_companies[0:
                (middle := len(it_companies)//2): 
                (last := len(it_companies))])

# 10) Print the list after modifying one of the companies
print(it_companies)
it_companies[0] = 'Meta'
print(it_companies)

# 11) Add an IT company to it_companies
print(it_companies)
it_companies.append('OpenAI')
print(it_companies)

# 12) Insert an IT company in the middle of the companies list
print(it_companies)
middle = len(it_companies)//2
it_companies.insert(middle, 'Anthropic')
print(it_companies)

# 13) Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies)
it_companies[0] = it_companies[0].upper()
print(it_companies)

# 14) Join the it_companies with a string '#;  '
lst_string = ['#']
print(together := it_companies + lst_string)

# 15) Check if a certain company exists in the it_companies list.
print('Facebook' in it_companies)

# 16) Sort the list using sort() method
print(it_companies.sort())

# 17) Reverse the list in descending order using reverse() method
print(it_companies.sort(reverse = True))

# 18) Slice out the first 3 companies from the list
print(it_companies)
print(it_companies[3:])

# 19) Slice out the last 3 companies from the list
print(it_companies)
print(it_companies[:-3])

# 20) Slice out the middle IT company or companies from the list
print(it_companies)
print(it_companies[(len(it_companies)-1)//2 : middle+1])

#21) Remove the first IT company from the list
print(it_companies)
print(it_companies.pop(0))

# 22) Remove the middle IT company or companies from the list
print(it_companies.pop(middle))

# 23) Remove the last IT company from the list
print(it_companies)
print(it_companies.pop(-1))

# 24) Remove all IT companies from the list
print(it_companies)
print(it_companies.clear())

# 25) Destroy the IT companies list
del it_companies
try:
    print(it_companies)

except NameError as e:
    print(f'Expected error: {e}')
print('And we continue!')

# 26) Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(both_ends := front_end + back_end)

# 27) After joining the lists in question 26. 
# Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = both_ends.copy()
full_stack.extend(['Python', 'SQL'])
print(full_stack)

# 28) The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 29) Sort the list and find the min and max age
print(ages.sort())
print(min(ages))
print(max(ages))

# 30) Add the min age and the max age again to the list
ages.extend([min(ages), max(ages)])
print(ages)

# 31) Find the median age (one middle item or two middle items divided by two)
ages = sorted(ages)

middle = len(ages) // 2

if len(ages) % 2 == 0:
    median = (ages[middle - 1] + ages[middle]) / 2
else:
    median = ages[middle]

print(median)

# 32) Find the average age (sum of all items divided by their number )
print(sum(ages)/len(ages))

# 33) Find the range of the ages (max minus min)
print(range := max(ages) - min(ages))

# 34) Compare the value of (min - average) and (max - average), use abs() method
print(min(ages)-(sum(ages))/len(ages), max(ages)-(sum(ages))/len(ages))

# 35) Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

if len(countries) % 2 == 0:
    middle = (int(len(countries)//2 - 1), int(len(countries)//2 + 1))
else:
    middle = len(countries)//2

print(countries[middle])

# 36) Divide the countries list into two equal lists if it is even if not one more country for the first half.
countries.insert(0, 'South Korea')
print(countries)

# 37)  Unpack the first three countries and the rest as scandic countries.
sk, chi, rus, us, *scandic = countries
print(sk, chi, rus, us, scandic)