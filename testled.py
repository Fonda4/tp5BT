import machine
import time

# Configuration des broches
RED_PIN = 11
GREEN_PIN = 12
BLUE_PIN = 13

# Initialisation des GPIO en mode sortie
red = machine.Pin(RED_PIN, machine.Pin.OUT)
green = machine.Pin(GREEN_PIN, machine.Pin.OUT)
blue = machine.Pin(BLUE_PIN, machine.Pin.OUT)

# Fonction pour définir la couleur de la LED
def set_color(r, g, b):
    red.value(r)    # 1 pour allumer, 0 pour éteindre
    green.value(g)
    blue.value(b)

# Liste des couleurs (rouge, vert, bleu, jaune, cyan, magenta, blanc, éteint)
colors = [
    (1, 0, 0),  # Rouge
    (0, 1, 0),  # Vert
    (0, 0, 1),  # Bleu
    (1, 1, 0),  # Jaune
    (0, 1, 1),  # Cyan
    (1, 0, 1),  # Magenta
    (1, 1, 1),  # Blanc
    (0, 0, 0),  # Éteint
]

try:
    while True:
        for color in colors:
            set_color(*color)
            time.sleep(1)  # Attente d'une seconde entre les couleurs

except KeyboardInterrupt:
    print("Arrêt du programme")

finally:
    set_color(0, 0, 0)  # Éteindre la LED
