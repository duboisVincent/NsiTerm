import turtle
turtle.speed(1000)
def koch(l,n):
                    # # Fractacle de Koch
    if n<=0:
        turtle.pendown
        turtle.forward(l)
        turtle.penup
    else:
        turtle.pendown
        koch(l/3,n-1)
        turtle.left(60)
        koch(l/3,n-1)
        turtle.right(120)
        koch(l/3,n-1)
        turtle.left(60)
        koch(l/3,n-1)
        turtle.penup
print(koch(100,3))
def flocon(l,n):
                    # # Flocon de Koch
    turtle.pendown
    koch(l,n)
    turtle.right(120)
    koch(l,n)
    turtle.right(120)
    koch(l,n)
    turtle.penup
print(flocon(100,3))