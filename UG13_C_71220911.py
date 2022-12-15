import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.pensize(8)
t.color('lime')
s.bgcolor('black')

#Inisial Depan
t.penup()
t.goto(-150,0)
t.pendown()
t.left(90)
t.forward(80)
t.left(180)
t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.forward(40)
t.left(180)
t.forward(80)

#NIM Tengah
t.penup()
t.goto(-50,0)
t.pendown()
t.left(180)
t.forward(80)
t.left(145)
t.forward(35)

#NIM Atas
t.penup()
t.goto(-75, 150)
t.left(35)
t.pendown()
t.circle(20, 180)
t.forward(40)
t.circle(20)

#NIM Bawah
t.penup()
t.goto(-50, -130)
t.pendown()
t.forward(80)
t.left(145)
t.forward(35)

#Inisial Belakang
t.penup()
t.goto(0,0)
t.left(125)
t.pendown()
t.left(90)
t.forward(80)
t.left(180)
t.forward(50)
t.left(90)
t.circle(25, 180)
t.hideturtle()



