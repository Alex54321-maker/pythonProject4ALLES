import pygame as pg

breite,spalten,zeilen = 400,10,20
abstand = breite//spalten
höhe = abstand//2*zeilen
grid = [0]*spalten*zeilen

bilder = []
for n in range(8):
    bilder.append(pg.transform.scale(pg.image.load(f"tt3_{n}.gif"),(abstand,abstand))
pg.init()
screen = pg.display.set_mode([breite,höhe])
grid[12]= 3
grid[13] = 3

weitermachen = True
while weitermachen:
    for event in pg.event.get():
        if event.type == pg.QUIT :
            weitermachen = False
        screen.fill((0,0,0))

pg.quit()
