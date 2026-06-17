import random  
realnumber = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print(f"I have selected a number between 1 and 100.")  
while True:

    try:
        guess = int(input("Enter your guess: "))
        if guess <= 0 or guess > 100:
           print("You fool! Select a number between 1 and 100 or I banish you to the library...")
        elif guess < realnumber:
            print(f"Too low! So bad so sad, why so mad? Try again.")
        elif guess > realnumber:
            print(f"Too high! So sigh so bye, why lie? Try again.")
        else:
            print(f"Congratulations! You are a genius! The number was {realnumber}. You guessed it right! ")
            break
    except ValueError:
        print("I said a number, not a word! Off to the Gulags with you! Try again.")

        