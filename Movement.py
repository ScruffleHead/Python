pos = [3, 3]
board = ["░░░░░░░",
         "░░░░░░░",
         "░░░░░░░",
         "░░░●░░░",
         "░░░░░░░",
         "░░░░░░░",
         "░░░░░░░"]

                                                                                                                #UNICODE CHARACTERS USED HERE: ░●
def draw():          #Draw() is the function that draws the board every time you move.
    counter = 0
    for i in range(0, len(board)):
        print(board[counter])
        counter = counter + 1


def move(direction):
    if direction == "left" and pos[0] != 0:
        index = pos[0]
        board[pos[1]]=board[pos[1]][:index] + "░" + board[pos[1]][index + 1:]
        board[pos[1]]=board[pos[1]][:index - 1] + "●" + board[pos[1]][index - 1 + 1:]
        pos[0] = pos[0] - 1
    elif direction == "right" and pos[0] != 6:
        index = pos[0]
        board[pos[1]]=board[pos[1]][:index] + "░" + board[pos[1]][index + 1:]
        board[pos[1]]=board[pos[1]][:index+1] + "●" + board[pos[1]][index+1 + 1:]
        pos[0] = pos[0] + 1
    elif direction == "up" and pos[1] != 0:
        index = pos[0]
        board[pos[1]]=board[pos[1]][:index] + "░" + board[pos[1]][index + 1:]
        board[pos[1] - 1]=board[pos[1] - 1][:index] + "●" + board[pos[1] - 1][index + 1:]
        pos[1] = pos[1] - 1
    elif direction == "down" and pos[1] != 6:
        index = pos[0]
        board[pos[1]]=board[pos[1]][:index] + "░" + board[pos[1]][index + 1:]
        board[pos[1] + 1]=board[pos[1] + 1][:index] + "●" + board[pos[1] + 1][index + 1:]
        pos[1] = pos[1] + 1
    else:
        print("Oops! You've bumped into a wall.")


while True:                                   #This is the main loop that activates all the movements and drawings when you do stuff.
    direction = input("WASD to move.")
    if direction == "w":
        move("up")
        draw()
    elif direction == "a":
        move("left")
        draw()
    elif direction == "s":
        move("down")
        draw()
    elif direction == "d":
        move("right")
        draw()
    else:
        print("Movement failed.")
