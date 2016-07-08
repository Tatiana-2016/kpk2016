from turtle import Turtle
default_scale = 3

def init_drawman():
    global t, x_current, y_current, _drawman_scale
    t = Turtle()
    t.penup()
    x_current = 0
    y_current = 0
    t.goto(x_current, y_current)
    drawman_scale(default_scale)

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


def draw_grid(_grid,_drawman_scale):
    """grid - задаваемая размерность сетки
    _drawman_scale - задаваемый масштаб
    """
    drawman_scale(_drawman_scale)
    pen_up()
    grid=_drawman_scale*_grid
    to_point(-grid,grid)
    pen_down()
    drawman_color("grey")
    x=0
    """Горизонтальная сетка
    """
    while x<=grid*2:
        on_vector(2*grid,0)
        pen_up()
        on_vector(-2*grid,-_drawman_scale)
        pen_down()
        x+=_drawman_scale
    pen_up()
    to_point(-grid,grid)
    pen_down()
    y=0
    """Вертикальная сетка
    """
    while y<=grid*2:
        on_vector(0,-2*grid)
        pen_up()
        on_vector(_drawman_scale,2*grid)
        pen_down()
        y+=_drawman_scale
    pen_up()
    """Рисуем ось х
    """
    drawman_color("black")
    to_point(-grid,0)
    pen_down()
    to_point(grid,0)
    pen_up()
    """Рисуем ось у
    """
    t.left(90)
    to_point(0,-grid)
    pen_down()
    to_point(0,grid)
    pen_up()
    """Переходим в начало координат
    """
    to_point(0,0)

init_drawman()
if __name__ == '__main__':
    import time
    pen_down()
    draw_grid(3,10)
    time.sleep(10)