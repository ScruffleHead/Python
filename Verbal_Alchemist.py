recipes={"air water":"mist",
         "air air":"atmosphere",
         "water water":"pond",
         "pond pond":"lake",
         "lake lake":"sea",
         "sea sea":"ocean",
         "land ocean":"planet",
         "fire fire":"energy",
         "energy energy":"sun",
         "earth fire":"lava",
         "earth lava":"volcano",
         "earth water":"mud",
         "fire mud":"clay",
         "earth earth":"land",
         "fire water":"steam",
         "air fire":"smoke",
         "air earth":"dust",
         "planet sun":"solar system",
         "solar system solar system":"galaxy",
         "galaxy galaxy":"universe", 
         "universe universe":"multiverse",       ## This is the list of all the recipes or combinations of elements in this game. Please ignore this if you don't want to cheat.
         "sun earth":"vegetation",
         "vegetation vegetation":"life",
         "air life":"bird",
         "bird bird":"egg",
         "air lava":"stone",
         "fire stone":"metal",
         "bird metal":"plane",
         "energy metal":"electricity",
         "electricity fire":"light",
         "life ocean":"fish",
         "fish metal":"submarine",
         "fish electricity":"eel",}
discovered=["air", "earth", "fire", "water"]

def ask():
    response=input("Please input two found elements. Add a space between the two elements, and the two elements must be in alphabetical order. Say \"LIST\" to see current list of elements.")
    if response.upper()=="LIST":
        print(discovered)
    elif response.lower() in recipes:
        discovered.append(recipes[response])
        print("You discovered %s!" % recipes[response])
    else:
        print("No new element discovered.")
    ask()
ask()
