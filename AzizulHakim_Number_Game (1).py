#CS106_Project_2
#Name: Azizul Hakim

#importing random module to use different guessing values each time we run the program
import random

#welcome prompt for the user
print("Guess the Number!\n")
print("I'm thinking of a number from 1 to 10\n")

#take input from user about their first guess

guess = random.randint(1,10)

#setting up variables for the loop

count = 0

#running the loop using while
while True:

    yourNumber = int(input("Your guess: "))
    count += 1

    if count<=10:
        if yourNumber == guess:
            print(f"You guessed it in {count} tries.")
            again = input("\nWould you like to play again? (y/n): ")
            if again == "y":
                guess = random.randint(1,10)
                count = 0
            elif again == "n":
                print("\nBye!")
                break
            else:
                print("Wrong keyword, run the game again.")
                break

        else:
            if yourNumber > guess:
                print("Too high.")
            elif yourNumber < guess:
                print("Too low.")

    elif count>10:
            print("\nYou have exceeded the limit of 10 Guesses")
            again = input("Would you like to play again? (y/n): ")
            if again == "y":
                count = 0
            elif again == "n":
                print("\nBye!")
                break
            else:
                print("Wrong keyword, run the game again.")
                break
