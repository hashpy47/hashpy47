import copy

name = "Alexander"
print(name[0])
print('Alex' in name)

for letter in name:
    print(letter)

name = 'Bob a builder'
print(name)
newName = name[:4] + 'the ' + name[5:]
print(newName)

#Lists

spam = [1, 2, 3, 4, 5]
cheese = spam
cheese[1] = "Hello"
print(cheese)
print(spam)

# If you wasnt a proper copy of a list , and not a copied, reference to a list, use deepcopy:
#import copy

coco = copy.deepcopy(spam)
coco[0] = 777

print("printing spam:")
print(spam)
print("printing coco:")
print(coco)

print("shows that deep copy makes a proper copy, and doesnt just reference copy")