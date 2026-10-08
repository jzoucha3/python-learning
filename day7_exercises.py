it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update('X', 'IG', 'Snapchat')
print(it_companies)

it_companies.remove('X')
print(it_companies)

print('The difference between remove and discard is remove raises an error if the item is not found in the set for removal and discard doesnt')

print(C := A.union(B))
print(C := A | B)

A.intersection(B)

A.issubset(B)

A.isdisjoint(B)

print(D := B.union(A))
print(C)

print(B.symmetric_difference(A))

del A
del B
del it_companies

print(len(age))
age = set(age)
print(type(age))

print('Strings are a sequence of characters and text')
print('Lists are a collection of values')
print('Tuples are a collection of values that are immutable')
print('A set is a collection of unique values')

sentence = 'I am a teacher and I love to inspire and teach people'
words = sentence.split()
print(words)
unique_words = set(words)
print(len(unique_words))
