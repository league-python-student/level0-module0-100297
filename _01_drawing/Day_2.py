import turtle

if __name__ == '__main__':
    window = turtle.Screen()

    Zach = turtle.Turtle()
    Zach.shape('turtle')
    Zach.color('red')
    a = 1

    for i in range(35):

        Zach.forward(a)
        Zach.right(90)

        for j in range(4):
            a = a + 1
            Zach.forward(a)
            Zach.left(90)

    turtle.done()
