import random

highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing
guess = 0
print(f"Please guess a number between 1 and {highest}: ")

while guess != answer:
    guess = int(input())

    if guess == 0:
        print("Game Over")
        break
    if guess == answer:
        print(f"{guess} is correct")
    else:
        if guess < answer:
            print(f"{guess} is incorrect, please guess higher")
        else:   # Must be higher
            print(f"{guess} is incorrect, please guess lower")
# if guess == 0:
#     print("Game Over")

