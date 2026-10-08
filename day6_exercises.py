#1) Create an empty tuple
empty_tuple = ()
print(empty_tuple)

# 2) Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
print(sister := ('lex',))
print(brother := ('aidan',))

# 3) Join brothers and sisters tuples and assign it to siblings
print(siblings := sister + brother)

# 4) How many siblings do you have?
print(len(siblings))

# 5) Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('theresa', 'hosea')
print(family_members := siblings + parents)

# 6) Unpack siblings and parents from family_members
*siblings, mother, father = family_members
parents = (mother, father)
print(siblings)
print(parents)

# 7) Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a 
# variable called food_stuff_tp.
fruits = ('cherry', 'mango')
veggies = ('carrot', 'broccoli')
animal = ('dairy', 'eggs')
print(food_stuff_tp := fruits + veggies + animal)

# 8) Change the about food_stuff_tp tuple to a food_stuff_lt list
type(list(food_stuff_tp))

# 9) Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

n = len(food_stuff_tp)

print(food_stuff_tp[(n - 1) // 2 : n // 2 + 1])

# 10) Slice out the first three items and the last three items from food_stuff_lt list
print(food_stuff_tp[:3] + food_stuff_tp[-3:])

# 11) Delete the food_stuff_tp tuple completely
del food_stuff_tp

try:
    print(food_stuff_tp)

except NameError as e:
    print(f'Expected error: {e}')
print('And we continue!')

#12) Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)

# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)