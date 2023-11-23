import turtle
from random import randint

t = turtle.Turtle()
turtle.colormode(255)
t.speed(8)
turtle.bgcolor("black")

def fiboFunc(lim):
    fib_series = [0, 1]
    while len(fib_series) < lim+2:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[1:]

def createRandColor(dark = True):
    lst = []
    if dark:
        for i in range(3):
            lst.append(randint(0,255//2))
    else:
        for i in range(3):
            lst.append(randint(255//2,255))
    return tuple(lst)

def CreateCurve(FibonacciSeries,radius,box = True,switch = False):
    for num in FibonacciSeries:
        t.pensize(2)                                        #Setting the pensize to 2
        t.pencolor(createRandColor(switch ^ True))          #creating a Random color, XORing with Switch
        t.circle(radius*num,90)                             #Creating the half Circle
        if box:
            for i in range(4):                                  #Crearing the box
                t.pencolor(createRandColor(switch ^ False))     
                t.pensize(1)
                t.left(90)
                t.forward(radius*num)

CreateCurve([i for i in range(20)],10,box=False,switch=True)

turtle.mainloop()