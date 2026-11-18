import pygame as pg

pg.init()

WIDTH, HEIGHT = 1000, 700
screen = pg.display.set_mode((WIDTH, HEIGHT))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        running = False

    pg.display.flip()

pg.quit()
