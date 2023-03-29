nine = ["▂▂▂▂▂▂▂▂▂▂▂▂▂",
        "▎            ▎",
        "▎            ▎",
        "▎          \😑/",
        "▎            ▎",
        "▎           /\ ",
        "▎",
        "▎▂▂▂▂▂▂"]

eight = ["▂▂▂▂▂▂▂▂▂▂▂▂▂",
     "▎            ▎",
     "▎            ▎",
     "▎           😑/",
     "▎            ▎",
     "▎           /\ ",
     "▎",
     "▎▂▂▂▂▂▂"]

seven = ["▂▂▂▂▂▂▂▂▂▂▂▂▂",
     "▎            ▎",
     "▎            ▎",           #This is just where I made all the hangman pictures. The top layer of all these lists being off-centre doesn't change anything, it's just an unintended inconvenience.
     "▎           😑",
     "▎            ▎",
     "▎           /\ ",
     "▎",
     "▎▂▂▂▂▂▂"]

six = ["▂▂▂▂▂▂▂▂▂▂▂▂▂",
     "▎            ▎",
     "▎            ▎",
     "▎           😑",
     "▎            ▎",
     "▎",
     "▎",
     "▎▂▂▂▂▂▂"]

five = ["▂▂▂▂▂▂▂▂▂▂▂▂▂",
     "▎            ▎",
     "▎            ▎",
     "▎           😑",
     "▎",
     "▎",
     "▎",
     "▎▂▂▂▂▂▂"]

four = ["▂▂▂▂▂▂▂▂▂▂▂▂▂",
     "▎            ▎",
     "▎            ▎",
     "▎",
     "▎",
     "▎",
     "▎",
     "▎▂▂▂▂▂▂"]

three = ["▂▂▂▂▂▂▂▂▂▂▂▂▂",
     "▎",
     "▎",
     "▎",
     "▎",
     "▎",
     "▎",
     "▎▂▂▂▂▂▂"]

two = [" ",
     "▎",
     "▎",
     "▎",
     "▎",
     "▎",
     "▎",
     "▎▂▂▂▂▂▂"]

one = [" ",
     " ",
     " ",
     " ",
     " ",
     " ",
     " ",
     "▂▂▂▂▂▂▂"]

zero = [" ",
     " ",
     " ",
     " ",
     " blank (like my brain lol)",
     " ",
     " ",
     " "]
              #Kinda annoying because the lists/images in this list are back to front (normally lists go up from zero but the names of the images go down)
stages = [nine, eight, seven, six, five, four, three, two, one, zero]

themes = {"puppy": "Animal",
         "giraffe": "Animal",
         "noodles": "Dish",
         "berlin": "Place",
         "india": "Place",
         "peanut": "Food",
         "orange": "Food",
         "gorilla": "Animal",
         "antarctica": "Place",
         "lemon": "Food",
         "whydidthechickencrosstheroad": "\"Famous\" song",
         "fishandchips": "Dish",
         "cluedo": "Game",
         "monopoly": "Game",
         "mouse": "Animal",
         "platypus": "Animal",
         "pastasoup": "Dish",
         "venus": "Place",}

words = ["puppy", "giraffe", "noodles", "berlin", "india", "peanut", "orange", "gorilla", "antarctica", "lemon", "whydidthechickencrosstheroad", "fishandchips", "cluedo", "monopoly", "mouse", "platypus", "pastasoup", "venus"]
letters = ["a", "b", "c", "d", "e", "f", 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', "z"]

############################################################################################################################

import random
gamemode = 0
while gamemode != 1 or gamemode != 2:
    response = input("Would you like to play two-player mode or with a randomly picked word from a list of %s words? say \"2\" for two player mode and \"1\" for one player. " % len(words))
    if response == "1":
        gamemode = 1
        break
    elif response == "2":                 #This bit just operates the gamemode-choosing thing at the start
        gamemode = 2
        break
    else:
        print("Response not recognised. Please try again.")

############################################################################################################################

def draw(displayedanswer, tries, wrongletters):
    print("█" * 40)
    for x in range(0, 8):
        print(stages[tries][x])
    print(" ")
    print(displayedanswer)
    print(" ")
    print("     WRONG LETTERS:")
    print(*wrongletters, sep=", ")
    print(" ")
    print("You have %s tries left." % tries)
    print("█" * 40)

############################################################################################################################

def rewrite(displayedanswer, answer, guessedletter):
    counter = 0
    newdis = ""
    for charofdisplayed in displayedanswer:
        if charofdisplayed == "_":                       #This function works by working through the current displayed answer, adding either the letters in the actual answer of more underscores to a new
            if answer[counter] == guessedletter:         #variable, then setting the current displayed answer to the new variable.
                newdis = newdis + guessedletter
            else:
                newdis = newdis + "_"
        else:
            newdis = newdis + charofdisplayed
        counter += 1
    return newdis
        

############################################################################################################################

def play_a_round():
    tries = 9
    guessedalready = []
    rightletters = []
    wrongletters = []
    if gamemode == 1:
        answer = words[random.randint(0, len(words)-1)]
        theme = themes[answer]
        print("Word chosen. The theme is %s." % theme)
    else:
        answer = input("Enter a word. No spaces please: ").lower()
        for x in range(0, 100):
            print("Hi there!")
    displayedanswer = "_" * len(answer)
    while True:                                          #This is where the main loop for singleplayer mode starts.
        guessedletter = input("Input a letter: ").lower()
        if guessedletter in letters:
            if not guessedletter in guessedalready:
                if guessedletter in answer:
                    displayedanswer = rewrite(displayedanswer, answer, guessedletter)
                    rightletters.append(guessedletter)
                    guessedalready.append(guessedletter)
                    draw(displayedanswer, tries, wrongletters)
                    if displayedanswer == answer:
                        print("Yay! You won!")
                        break
                else:
                    wrongletters.append(guessedletter)
                    guessedalready.append(guessedletter)
                    tries = tries - 1
                    draw(displayedanswer, tries, wrongletters)
                    if tries == 0:
                        print("You lost! The word was %s!" % answer)
                        break
            else:
                print("You already guessed this.")
                continue
while True:
    play_a_round()
