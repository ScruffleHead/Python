lvl1row0 = ["█", "█", "█", "█", "█"]       #This is the layout of the board. Ignore the fact that everything is called "lvl1", I'm not planning on making more levels.
lvl1row1 = ["█", " ", " ", " ", "█"]
lvl1row2 = ["█", " ", "█", "█", "█"]
lvl1row3 = ["█", " ", " ", " ", "█"]
lvl1row4 = ["█", "█", "█", " ", "█"]
lvl1row5 = ["█", "△", " ", " ", "█"]
lvl1row6 = ["█", "█", "█", "█", "█"]


lvl1 = (lvl1row0, lvl1row1, lvl1row2, lvl1row3, lvl1row4, lvl1row5, lvl1row6)


pos = [1, 5]


fin = [3, 1]
axis = "x"


def move(direction):
    if direction == "left":
        if axis == "x":
            if lvl1[pos[1]][pos[0]-1] == "█":
                print("Bump!")
            else:
                lvl1[pos[1]][pos[0]] = " "
                lvl1[pos[1]][pos[0]-1] = "△"
                pos[0] = pos[0] - 1
                draw()
        else:
            if lvl1[pos[1]-1][pos[0]] == "█":
                print("Bump!")
            else:
                lvl1[pos[1]][pos[0]] = " "
                lvl1[pos[1] - 1][pos[0]] = "△"
                pos[1] = pos[1] - 1
                draw()
    else:
        if axis == "x":
            if lvl1[pos[1]][pos[0]+1] == "█":
                print("Bump!")
            else:
                lvl1[pos[1]][pos[0]] = " "
                lvl1[pos[1]][pos[0]+1] = "△"
                pos[0] = pos[0] + 1
                draw()
                if pos == fin:
                    print("Yay! You won!")
        else:
            if lvl1[pos[1]+1][pos[0]] == "█":
                print("Bump!")
            else:
                lvl1[pos[1]][pos[0]] = " "
                lvl1[pos[1] + 1][pos[0]] = "△"
                pos[1] = pos[1] + 1
                draw()


def draw():
    if axis == "x":
        print(*lvl1[pos[1]], sep = "")
        if pos[1] == fin[1]:
            print("███▞█")
        else:
            print("█████")
    else:
        Zstring = lvl1row0[pos[0]] + lvl1row1[pos[0]] + lvl1row2[pos[0]] + lvl1row3[pos[0]] + lvl1row4[pos[0]] + lvl1row5[pos[0]] + lvl1row6[pos[0]]
        print(Zstring)
        if pos[0] == fin[0]:
            print("█▞█████")
        else:
            print("███████")


draw()


while True:
    response = input("A and D to move, leave blank to switch dimensions.")
    if response == "a":
        move("left")
    elif response == "d":
        move("right")
    elif response == "" and axis == "x":
        axis = "z"
        print("Dimensions switched to Z.")
        draw()
    elif response == "" and axis == "z":
        axis = "x"
        print("Dimensions switched to X.")
        draw()
    else:
        print("Unrecognised response.")
