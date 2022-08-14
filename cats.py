print("How many cats o you have?")
numb_cats = input()

try:
    if int(numb_cats) > 4:
        print("Too many cats dude.")
    else:
        print("less than 4 is still too many")
except ValueError:
    print("You did not enter a number.")
