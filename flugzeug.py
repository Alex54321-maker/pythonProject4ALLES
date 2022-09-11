import pygame
from pygame.locals import *
pygame.init()

# Variablen/KONSTANTEN setzen
W, H = 800, 600

W_HALBE = W / 2
H_HALBE = H / 2

FPS  = 60
SCHWARZ    = (  0,   0,   0)
WEISS      = (255, 255, 255)
GRAU       = (155, 155, 155)
HIMMELBLAU = (120, 210, 255)
spielaktiv = True

gradzahl = 0

propeller = pygame.image.load("img/propeller.png")
flugzeugrumpf = pygame.image.load("img/propellerflieger.png")

# Definieren und Öffnen eines neuen Fensters
fenster = pygame.display.set_mode((W, H))
pygame.display.set_caption("www.Python-lernen.de - Grafiken rotieren")
clock = pygame.time.Clock()

# Funktion zum Grafiken rotieren und zentrieren
# def rotieren_zentrieren(ausgabe, x, y, bild, gradangabe):
def rotieren_zentrieren(x, y, bild, gradangabe):
    # rotieren und in einem neuen "surface" speichern
    rotiert = pygame.transform.rotate(bild, gradangabe)

    # Bestimmen der neuen Abmessungen (nach Rotation ändern sich diese!)
    groesse = rotiert.get_rect()

    # Ausgabe
    fenster.blit(rotiert, (x - groesse.center[0],y - groesse.center[1]))

    # Viereck zur Kontrolle zeichnen
    pygame.draw.rect(fenster, (255, 255, 255), (x - groesse.center[0], y - groesse.center[1], groesse.width, groesse.height), 1)

def rotieren(x, y, bild, gradangabe):
    rotiert = pygame.transform.rotate(bild, gradangabe)
    fenster.blit(rotiert, (x, y))

    # Viereck zeichnen - erst Größe ermitteln
    viereck = rotiert.get_rect()
    pygame.draw.rect(fenster, (200, 0, 0), (x, y, viereck.width, viereck.height), 1)

# Schleife Hauptprogramm
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        # Beenden bei [ESC] oder [X]
        if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
            spielaktiv = False

    # Spiellogik
    if gradzahl <= 359:
        gradzahl += 5
    else:
        gradzahl = 0

    # Spielfeld löschen
    fenster.fill(HIMMELBLAU)

    # Spielfeld/figuren zeichnen
    fenster.blit(flugzeugrumpf, (20, 30))
    # rotieren(118, 32, propeller, gradzahl)
    rotieren_zentrieren(118+50, 32+31, propeller, gradzahl)

    # Fenster aktualisieren
    pygame.display.flip()
    clock.tick(FPS)
