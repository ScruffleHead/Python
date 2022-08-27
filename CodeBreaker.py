import random
letters = ["A", "B", "C", "D", "E", "F", "G"]
code = []
guess = []
tries = 4
check = []
    

print('''Welcome to codebreaker!
You will have four tries to guess the five - letter code.
The code will be made up of five of the first seven letters of the alphabet in a random order.
After you put in your guess, the game will show you five boxes.
If a box is blank, that means the digit you guessed directly above it is nowhere in the code.
If a box is grey, the guessed digit above it is in the code, but not in the right place.
If a box is black, its digit is in the correct place in the code.
Also, guesses must be in capitals.''')


while True:
    code = []
    iamauselessvariable = input("Press enter to begin.")
    while len(code) <= 4:
        num = random.randint(0, 6)
        if not letters[num] in code:
            code.append(letters[num])
    tries = 4
    while guess != code or tries != 0:
        if tries == 0:
            print("You ran out of tries! The code was ", *code)
            break
        inpt = input("%s tries left. Enter your guess:" % tries)
        if len(inpt) == 5:
            valid = True
            guess = list(inpt)
            for i in range(0, 5):
                if not guess[i] in letters:
                    print("Your guess must be made up of A, B, C, D, E, F and/or G.")
                    valid = False
                    break
            if valid == False:
                continue
            check=[]
            for h in range(0, 5):
                if guess == code:
                    print("You got it!")
                    break
                elif guess[h] == code[h]:
                    check.append("█")
                elif guess[h] in code:
                    check.append("▒")
                else:
                    check.append("□")
            if guess == code:
                break
            guess = []
            tries = tries - 1
            if tries > 0:
                print(*check)
        else:
            print("Your guess must be five letters long.")
