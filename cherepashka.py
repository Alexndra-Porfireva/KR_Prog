import pygame as pg

pg.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

COLOR_LINE = WHITE

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Черепашка")
screen.fill(WHITE)

x1, x2 = 300, 300
y1, y2 = 300, 300
cmds = [x1, y1], [x2, y2]

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    pg.draw.line(screen, COLOR_LINE, cmds[0], cmds[1], 3)
    pg.display.update()

    user = input()
    yser = user.split()
    user_up = user.startswith("up")
    user_down = user.startswith("down")
    user_left = user.startswith("left")
    user_right = user.startswith("right")
    user_goto = user.startswith("goto")
    user_tail = user.startswith("tail")
    if user_tail == True:
        user_tail_up = user.endswith("up")
        if user_tail_up == True:
            COLOR_LINE = BLACK

        elif user_tail_up == False:
            exit()
    else:
        if user_up == True:
            x1 = x2
            y1 = y2
            y2 -= float(yser[-1])
            pg.draw.line(screen, COLOR_LINE, [x1, y1], [x2, y2], 3)

        elif user_down == True:
            x1 = x2
            y1 = y2
            y2 += float(yser[-1])
            pg.draw.line(screen, COLOR_LINE, [x1, y1], [x2, y2], 3)

        elif user_left == True:
            x1 = x2
            y1 = y2
            x2 -= float(yser[-1])
            pg.draw.line(screen, COLOR_LINE, [x1, y1], [x2, y2], 3)

        elif user_right == True:
            x1 = x2
            y1 = y2
            x2 += float(yser[-1])
            pg.draw.line(screen, COLOR_LINE, [x1, y1], [x2, y2], 3)

        elif user_goto == True:
            x1 = x2
            y1 = y2
            x2 = float(yser[-2])
            y2 = float(yser[-1])
            pg.draw.line(screen, COLOR_LINE, [x1, y1], [x2, y2], 3)
pg.quit()
quit()

