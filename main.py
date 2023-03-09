'''
"Circus"
Group:
Tsvykh Viktoria
Fishchukova Sofia
'''

import turtle
def triangle(x, y, a, b, angle, color):
    '''
    Function for drawing triangle.
    :param x:
    :param y:
    :param a:
    :param b:
    :param angle:
    :param color:
    :return:
    '''

    pass

def ellipse(x, y, a, b, color, fill, pensize):
    '''
    Function for draw ellipse.
    :param x: x start coordinate
    :param y: y start coordinate
    :param a: axis length on x-axis
    :param b: axis length on y-axis
    :param color: stroke color
    :param fill: fill color
    :param pensize: pensize
    :return:
    '''

    turtle.color(color, fill)
    turtle.begin_fill()
    turtle.pensize()
    turtle.pu()
    turtle.goto(x, y)
    turtle.rt(45)
    turtle.pd()

    for i in range(2):
        turtle.circle(a, 90)
        turtle.circle(b, 90)

    turtle.end_fill()
    turtle.done()


def quadrilateral(x, y, a, b, angle1, angle2, color, fill):
    '''
    Function for draw quadrilateral.
    :param x:      x start coordinate
    :param y:      y start coordinate
    :param a:      length of side parallel to x-axis
    :param b:      length of side parallel to y-axis
    :param angle1: bottom right and top left angles
    :param angle2: top right and bottom left angles
    :param color:  stroke color
    :param fill:   fill color
    :return:
    '''

    turtle.color(color, fill)
    turtle.begin_fill()
    turtle.pu()
    turtle.goto(x, y)
    turtle.pd()

    for i in range(2):
        turtle.fd(a)
        turtle.lt(angle1)
        turtle.fd(b)
        turtle.lt(angle2)

    turtle.end_fill()
    turtle.done()


def draw_elephant():
    '''Drawing funny elephant on big ball'''

    pass

def draw_clown():
    '''Drawing clown with balls'''

    pass

def main():
    '''
    Main function.
    :return:
    '''
    draw_elephant()
    draw_clown()


if __name__ == '__main__':
    main()
    