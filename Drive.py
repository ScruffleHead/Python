###########################################################################               SETTING VARIABLES AT THE START

from tkinter import*
import time
import random
tk = Tk()
tk.title("Drive - v1.0 - Made by ScruffleHead")
tk.resizable(0, 0)
canvas = Canvas(tk, width=400, height=500, bd=0, highlightthickness=0)
canvas.pack()
bg1 = canvas.create_rectangle(0, 0, 400, 500, fill="green")        # Making the grass outside of the road
bg2 = canvas.create_rectangle(80, 0, 320, 500, fill="#808080")     # Making the road
x_positions = [90, 165, 240]                                       # This list contains the three X positions that bad cars can generate with.
gameover = False                                                   # This boolean variable will be set to True when the game ends, which stops all the code.

###########################################################################               MAIN CAR

class Car:
    def __init__(self, canvas):
        self.canmove = True         #This variable stops you moving one way while you're in the middle of moving another way.
        self.pos = "Centre"         #Obviously this one is which lane you're in
        self.canvas = canvas
        self.Image1 = PhotoImage(file="~/Desktop/Python/Assets/Drive Assets/redcar.gif")
        self.id = canvas.create_image(165, 250, anchor=NW, image=self.Image1)
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)


    def turn_right(self, evt):                               # turn_right and turn_left are in charge of switching lanes when you press left or right.
        if self.pos == "Centre" and self.canmove == True:
            self.canmove = False
            self.canvas.move(self.id, 40, 0)
            tk.update()
            time.sleep(0.02)
            self.canvas.move(self.id, 35, 0)
            self.pos = "Right"
            self.canmove = True
        elif self.pos == "Left" and self.canmove == True:
            self.canmove = False
            self.canvas.move(self.id, 40, 0)
            tk.update()
            time.sleep(0.02)
            self.canvas.move(self.id, 35, 0)
            self.pos = "Centre"
            self.canmove = True

    def turn_left(self, evt):
        if self.pos == "Centre" and self.canmove == True:
            self.canmove = False
            self.canvas.move(self.id, -40, 0)
            tk.update()
            time.sleep(0.02)
            self.canvas.move(self.id, -35, 0)
            self.pos = "Left"
            self.canmove = True
        elif self.pos == "Right" and self.canmove == True:
            self.canmove = False
            self.canvas.move(self.id, -40, 0)
            tk.update()
            time.sleep(0.02)
            self.canvas.move(self.id, -35, 0)
            self.pos = "Centre"
            self.canmove = True

###########################################################################                   BAD CARS

class Badcar:                                                      #The badcars are the blue cars that are going the opposite way as you that you need to avoid.
    def __init__(self, canvas, x_positions, car, gameover):
        self.x_positions = x_positions                             #This list contains the three x positions of the three lanes. When the badcar is created, it picks a random one of these.
        self.car = car
        self.canvas = canvas
        self.Image2 = PhotoImage(file="~/Desktop/Python/Assets/Pixel_PlatformerDrive Assets/bluecar.gif")
        self.id = canvas.create_image(0, 0, anchor=NW, image=self.Image2)
        self.canvas.move(self.id, self.x_positions[random.randint(0, 2)], -100)
    def hit_car(self, pos):                 # hit_car detects if it has hit the car by comparing the coordinates of the badcars and the main car.
        carpos = self.canvas.coords(self.car.id)
        if carpos[0] == pos[0]:
            if pos[1] <= carpos[1]+120 and carpos[1] <= pos[1]+120:
                return True
        return False
    def draw(self):                         # draw controls the movement of the badcars.
        self.canvas.move(self.id, 0, 12)
        pos = self.canvas.coords(self.id)
        if self.hit_car(pos) == True:
            global gameover
            gameover = True

###########################################################################                   MAIN LOOP

time.sleep(3)
car = Car(canvas)
badcar1 = Badcar(canvas, x_positions, car, gameover)
badcar2 = Badcar(canvas, x_positions, car, gameover)
while True:                        # Just the main loop.
    for x in range(0, 50):
        badcar1.draw()
        badcar2.draw()
        time.sleep(0.01)
        tk.update()
        if gameover == True:
            break
    if gameover == True:
        quit()                  # quit() stops everything happening in the game, which ends it.
    del badcar1
    del badcar2
    badcar1 = Badcar(canvas, x_positions, car, gameover)
    badcar2 = Badcar(canvas, x_positions, car, gameover)
