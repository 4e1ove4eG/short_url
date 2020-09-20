import turtle
t = turtle.Pen()
t.speed("fast")
ts = t.getscreen()
for x in range(255):
    ts.colormode(255)
    #t.pencolor(x,x,255 - x)
    t.circle(x)
    #t.left(100)
