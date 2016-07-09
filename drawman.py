from turtle import Turtle
default_scale = 1

def init_drawman():
    global t, x_current, y_current, _drawman_scale
    t = Turtle()
    t.penup()
    x_current = 0
    y_current = 0
    t.goto(x_current, y_current)
    drawman_scale(default_scale)
    t.speed(30)

def drawman_color(color):
    t.color(color)


def drawman_scale(scale):
    global _drawman_scale
    _drawman_scale = scale

def pen_down():
    t.pendown()

def pen_up():
    t.penup()


def on_vector(dx, dy):
    to_point(x_current + dx, y_current + dy)


def to_point(x, y):
    global x_current, y_current
    x_current = x
    y_current = y
    t.goto(_drawman_scale*x_current, _drawman_scale*y_current)


def draw_grid(_setka,mashtab):
    """setka - задаваемая размерность сетки
    mashtab - задаваемый масштаб
    """
    pen_up()
    setka=mashtab*_setka
    to_point(-setka,setka)
    pen_down()
    drawman_color("grey")
    x=0
    """Горизонтальная сетка
    """
    while x<=setka*2:
        on_vector(2*setka,0)
        pen_up()
        on_vector(-2*setka,-mashtab)
        pen_down()
        x+=mashtab
    pen_up()
    to_point(-setka,setka)
    pen_down()
    y=0
    """Вертикальная сетка
    """
    while y<=setka*2:
        on_vector(0,-2*setka)
        pen_up()
        on_vector(mashtab,2*setka)
        pen_down()
        y+=mashtab
    pen_up()
    """Рисуем ось х
    """
    drawman_color("black")
    to_point(-setka,0)
    pen_down()
    for i in range(-_setka,_setka+1):
        t.write(i)# подписываем ось х
        on_vector(mashtab,0)
    to_point(setka+mashtab,0)
    init_drawman()
    pen_up()
    """Рисуем ось у
    """
    to_point(0,-setka)
    pen_down()
    for i in range(-_setka,_setka+1):
        t.write(i)#подписываем ось у
        on_vector(0,mashtab)
    to_point(0,setka+mashtab)
    t.left(90)
    init_drawman()

    pen_up()
    """Переходим в начало координат
    """
    drawman_color("red")
    to_point(0,0)


init_drawman()
if __name__ == '__main__':
    import time
    pen_down()
    draw_grid(10,30)
    time.sleep(20)