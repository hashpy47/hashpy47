spam = ['hi', 'hello', 'howdy', 'whatsup']
print(spam.index('hello'))
spam.append("howzit")
spam.insert(0,'greetings')
#spam.remove('hi')
del spam[-1]    #deletes using index, not value

spam.sort(key=str.lower)    # in ascii, CAPS comes before lower case, so this will lowercase sort them, so its sorted properly
print(spam)
spam.sort(reverse=True)
print(spam)


