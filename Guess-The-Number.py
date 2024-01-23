import random

def guess_the_number():
    # Generate a random number between 1 and 100 (inclusive)
    secret_number = random.randint(1, 100)

    print("Welcome to the 'Guess the Number' game!")
    print("I have chosen a number between 1 and 100.")
    print("Try to guess the number!")

    attempts = 0
    while True:
        try:
            # Get user input as an integer
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess == secret_number:
                print(f"Congratulations! You guessed the correct number ({secret_number}) in {attempts} attempts!")
                break
            elif user_guess < secret_number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    guess_the_number()