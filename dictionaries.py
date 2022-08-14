spam = {'name': 'Kathy', 'age': 27, 'species' : 'human'}
eggs = {'age': 27, 'name': 'Kathy','species' : 'human'}

print("checking if the key exists in dict")
print(spam['name'])


print('age' in spam)
print('\n')

print("Is spam = to eggs")
print(spam == eggs)
print('\n')

print("print keys")
print(list(eggs.keys()))
print('\n')

print("print values")
print(list(eggs.values()))
print('\n')

print("print items")
print(list(eggs.items()))
print('\n')
print("For Loop with keys:")

for k in eggs.keys():
    print(k)
print('\n')
print("For Loop with values:")
for v in eggs.values():
    print(v)
print('\n')
print("key and value variables in 1 for loop:")
for k,v in eggs.items():
    print("The Key: " + str(k) + ".The Value: " + str(v) + ".")

print('\n')
print("to prevent key error:")
if 'age' in eggs:
    print(eggs['age'])
print('\n')
#get() is used to check if the key is there, and lets you put a default value if it doesnt exist

print("eggs.get('dangle','No dangle found'):   \n" + str(eggs.get('dangle', 'No dangle found')))

ham = {'name': 'Zophie', 'species': 'cat', 'age': 8}

#if 'colour' not in ham:        You can do this with the default
#    ham['colour'] = 'black'

ham.setdefault('colour', 'black')
print(ham)