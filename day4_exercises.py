thirty = 'thirty'
days = 'days'
of = 'of'
python = 'python'
print(together := thirty+days+of+python)

coding = 'coding'
ffor = 'for'
alll = 'all'
print(altogether := coding+ffor+alll)

print(company := 'coding for all')

print(len(company))

print(company.upper())

print(company.lower())

print(company.title().swapcase())

print(company[6:])

print(company[0:6])

print(company.replace('coding', 'python'))

p4e = ('python for everyone')
print(p4e.replace( 'everyone','all'))

print(company.split())

companies = ('facebook, google micrsofot, apple ibm, oracle, amazon')
print(companies.split(', '))

print(company[0])

print(company[-1])

print(company[10])

p_i = int(p4e.find('p'))
f_i = int(p4e.find('f'))
e_i = int(p4e.find('e'))
p =str( p4e[p_i])
f = str(p4e[f_i])
e = str(p4e[e_i])
print(p.capitalize() + f.capitalize() + e.capitalize())

c_i = int(company.find('p'))
f_i = int(company.find('f'))
a_i = int(company.find('e'))
c = str(company[c_i])
f = str(company[f_i])
a = str(company[a_i])
print(c.capitalize() + f.capitalize() + a.capitalize())

# Practiced 20-22 already by way the last two are done

sentence = 'you cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

print(sentence.rindex('because'))

print(sentence.replace('because', ' '))

print(company.startswith('Coding'))

print(company.startswith('coding'))

spaces = ' coding for all '
print(spaces.strip(' '))


dop = '30daysofpython'
tdop = 'thirtydaysofpython'
print(dop.isidentifier())
print(tdop.isidentifier())

libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('-'.join(libs))

print(multiline := '''I am enjoying this challenge.
I just wonder what is next''')

print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinalnd\tHelsinki')

radius = 10
area =- 3.14 * radius ** 2
print(formatted := 'The area of a circle with radius %d is %.2f meters.' %(radius, area))


a = '8 + 6 = 14'
b = '8 - 6 = 2'
c = '8 * 6 = 48'
d = '8 / 6 = 1.33'
e = '8 % 6 = 2'
f = '8 // 6 = 1'
g = '8 ** 6 = 262144'
print(f"{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}")
