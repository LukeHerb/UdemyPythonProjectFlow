name = str(input("What is your name? "))
age = int(input("How old are you {}? ".format(name)))

if 18 <= age < 31:
    print("Welcome to the holiday, {}".format(name))
else:
    print("Sorry, {}, you are not invited to the holiday".format(name))
