import turtle

turtle.left(90)

def tree(n: int):
    if n == 0:
        return
    turtle.forward(25 * n)

    turtle.left(30)
    tree(n - 1)
    turtle.right(30)
    
    turtle.right(30)
    tree(n - 1)
    turtle.left(30)

    turtle.backward(25 * n)

tree(4)

turtle.update()
turtle.done()