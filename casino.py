secret = 17

guess = int(input("Guess the secret number (0-20): "))

if guess == secret:
    print("Congratulations, you've won a million euros!")
else:
    print("The secret number is not " + str(guess) + ". " + "Try again tomorrow!")