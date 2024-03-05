import turtle
screen=turtle.Screen()
tess=turtle.Turtle()
tess.shape("turtle")
for i in range(4):
    tess.color(input("please enter your color:"))
    tess.forward(float(input("please enter lenght:")))
    tess.right(90)
turtle.mainloop()    