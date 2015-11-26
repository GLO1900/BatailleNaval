import turtle

def tracerClic(x, y):
    fen.onclick(None, btn=1)
    alex.setheading(alex.towards(x, y))
    alex.goto(x, y)
    fen.onclick(tracerClic, btn=1)

def changerModeEcriture():
    fen.onkeypress(None, 'space')
    if alex.isdown():
        alex.penup()
        alex.fillcolor('white')
    else:
        alex.pendown()
        alex.fillcolor('black')
    fen.onkeypress(changerModeEcriture, 'space')

fen = turtle.Screen()
fen.setup(width=500, height=500)
fen.onclick(tracerClic, btn=1)
fen.onkeypress(changerModeEcriture, 'space')
fen.listen()
alex = turtle.Turtle()
fen.mainloop()