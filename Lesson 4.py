import turtle as t
import random 

t.bgcolor("#2aa4f5")
t.speed(0)

t.penup()
t.goto(-380, -130)
t.pendown()

t.color("black", "#c27f04")
t.begin_fill()
for x in range (2):
    t.forward (753)
    t.right(90)
    t.forward(230)
    t.right(90)
t.end_fill()

for x in range (30):
    t.penup()
    x = random.randint (-380, 373)
    y = random.randint (-360, -130)
    t.goto(x,y)
    t.pendown()
    t.color("#614004")
    t.dot(5)

#pyramid

t.penup()
t.goto(-240,-130)
t.pendown()
t.setheading(55)
t.width(3)
t.color("#e0a538")
t.begin_fill()
t.forward(240)
t.setheading(305)
t.forward(240)
t.end_fill()

t.penup()
t.width(6)
t.setheading(0)
t.color("black")
t.goto(-206,-80)
t.pendown()
t.forward(209)
t.penup()
t.goto(-158,-10)
t.pendown()
t.forward(114)

t.mainloop()