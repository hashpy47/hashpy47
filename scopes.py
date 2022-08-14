def spam():
    global eggs
    print(eggs)
    eggs= 1
    print(eggs)
eggs = 42
spam()
print(eggs)
