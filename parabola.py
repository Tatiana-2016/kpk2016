from drawman import *

def f(x):
    return x*x

if __name__ == '__main__':
    import time
    pen_down()
    setka=10
    mashtab=30
    draw_grid(setka,mashtab)

    x = -3.0
    to_point(x*mashtab, mashtab*f(x))
    drawman_color("green")
    pen_down()
    while x <= 3:
        to_point(x*mashtab, mashtab*f(x))
        x +=0.01
    pen_up()
    time.sleep(10)