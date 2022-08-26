from random import randint

answer = randint(1, 100)

while int(input("Guess a number between 1 and 100: ")) != answer:

    print("Your guess is too low." if guess < answer else "Your guess is too high.")
        
print("Yay! You won!")
