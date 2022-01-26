# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
#
# for item in shopping_list:
#     if item == "spam":
#         break
#
#     print("Buy " + item)

for i in range(1, 21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    else:
        print(i)