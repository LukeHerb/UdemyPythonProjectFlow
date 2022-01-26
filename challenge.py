# write a program to input a number of options
# allow user to select an option from the list
# At least 4 options
# sample output:
# 1. Learn python
# 2. Learn Java
# 3. Go Swimming
# 4. Have Dinner
# 5. Go to bed
# 0. Exit

# list_of_options = ["1. Learn Python", "2. Learn Java", "3. Go Swimming", "4. Have Dinner",
#                    "5. Go to bed", "0. Exit"]
# user_selection = ""
#
# while user_selection != "0":
#     print(list_of_options)
#     user_selection = input("Please select an activity above ")
#     if user_selection != "0":
#         print(f"{user_selection} Sounds like fun, what else do you want to do? ")
# else:
#     print("Have a good day")


choice = "-"
while choice != "0":
    if choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please choose your options from the list below:")
        print("1:\t Learn Python")
        print("2:\t Learn Java")
        print("3:\t Go swimming")
        print("4:\t Have dinner")
        print("5:\t Go to bed")
        print("0:\t Exit")
    choice = input()

for x in range(30):
    if x % 3 == 0 or x % 5 == 0:
        print(x)

print("*" * 80)

for x in range(30):
    if x % 3 != 0 and x % 5 != 0:
        print(x)