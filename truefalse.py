day = "Friday"
temperature = 30
raining = False

if (day == "Saturday" and temperature > 27) or not raining:
    print("Go swimming")
else:
    print("Learn Python")

if 0:
    print("True")
else:
    print("False")

name = input("Please Enter Your Name: ")

# if name:
if name != "":
    print(f"Hello, {name}")
else:
    print("Are you the man with no name")
