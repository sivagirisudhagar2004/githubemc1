
import turtle
import time

WIDTH,HEIGHT = 500,500
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Turtle Racing!")


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

def init_turtle():
      screen = turtle.Screen()
      screen.setup(WIDTH, HEIGHT)
      screen.title("Turtle Racing!")
      
racers = get_number_of_racers()
init_turtle()


racer = turtle.Turtle()

racer.speed(1)
racer.penup()
racer.shape("turtle")
racer.color("red")
racer.forward(100)
racer.left(90)
racer.pendown()
racer.forward(100)
racer.right(90)
racer.backward(100)

racer2 = turtle.Turtle()

racer2.speed(5)
racer2.penup()
racer2.shape("turtle")
racer2.color("black")
racer2.forward(150)
racer2.left(90)
racer2.pendown()
racer2.forward(150)
racer2.right(90)
racer2.backward(150)

racer3 = turtle.Turtle()

racer3.speed(10)
racer3.penup()
racer3.shape("turtle")
racer3.color("yellow")
racer3.forward(200)
racer3.left(90)
racer3.pendown()
racer3.forward(200)
racer3.right(90)
racer3.backward(200)