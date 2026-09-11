import turtle
import time
import random

width, height = 500, 500
COLORS = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "gray", "cyan"]

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
                print("Input is not numeric...Try Again!")
                continue
        if (2 <= racers <= 10):
                return racers
        else:
                print("Number not in range 2-10.Try Again!")

def race(colors):
    turtles =   create_turtle(colors)

    while True:
          for racers in turtles:
                distance = random.randrange(1,20)
                racers.forward(distance)


                x,y = racers.pos()
                if (y >= height//2 - 10):
                      return colors[turtles.index(racers)]
                

def create_turtle(colors):
      turtles = []
      specingx =  width // (len(colors) + 1)
      for i ,color in enumerate(colors):
            racers = turtle.Turtle()
            racers.color(color)
            racers.shape("turtle")
            racers.left(90)
            racers.penup()
            racers.setpos(-width//2 + (i + 1) * specingx , -height//2 + 20)
            racers.pendown()
            turtles.append(racers)

      return turtles

def init_turtle():
        screen = turtle.Screen()
        screen.setup(width, height)
        screen.title("Turtle Racing!")

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]


winner = race(colors)
print("The Winner is the turtle with color:",winner)
time.sleep(5)

