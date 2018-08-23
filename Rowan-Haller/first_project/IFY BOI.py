import random

computer_number = random.randrange(0, 101)
print(computer_number)

guessed = False

while True:
    if guessed:
        answer = input("Guess the number ")
        if int(answer) == computer_number:
            guessed = True
            print("You got it!")
            break
        elif int(answer) > computer_number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")

    else:
        break