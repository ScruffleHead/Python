import random
guess=None
answer=random.randint(1, 100)
while guess != answer:
    guess=int(input("Guess a number between 1 and 100."))
    if guess==answer:
        break
    elif guess < answer:
        print("Your guess is too low.")
    elif guess > answer:
        print("Your guess is too high.")
    else:
        print("Please input an integer.")
print("Yay! You won!")
