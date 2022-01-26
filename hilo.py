low = 1
high = 1000
print(f"Please think of a number between {low} and {high}")
input("When you have your number, press Enter to start")
guesses = 1
while low != high:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter H if your number is higher than my guess,"
                     " or L if your number is lower than my guess, "
                     "or C if my guess is correct "
                     .format(guess).casefold())
    if high_low == "h":
        # Guess needs to be higher. The low end of the range becomes one greater than the guess.
        low = guess + 1
    elif high_low == "l":
        # Guess needs to be lower. The high end of the range becomes one less than the guess.
        high = guess - 1
    elif high_low == "c":
        # Guess is correct.
        print(f"I got it in {guesses} guesses!")
        break
    else:
        print("Please Enter H, L or C")

    guesses += 1
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))



