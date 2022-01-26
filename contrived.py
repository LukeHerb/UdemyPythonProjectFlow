numbers = [1, 25, 31, 16, 60]

for number in numbers:
    if number % 8 == 0:
        # reject the list
        print("Numbers are unacceptable")
        break
else:
    print("All those numbers are fine")

