from drawman import *


def f(x):
    return x*x*x

if __name__ == '__main__':
    import time
    pen_down()
    setka=10
    mashtab=20
    draw_grid(setka,mashtab)

    x = -5.0
    to_point(x*mashtab, mashtab*f(x))
    pen_down()
    while x <= 5:
        to_point(x*mashtab, mashtab*f(x))
        x +=0.1
    pen_up()
    time.sleep(30)