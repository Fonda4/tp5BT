from machine import UART, Pin
import time

# Configuration de l'UART sur le GPIO 0 (TX) et GPIO 1 (RX) pour le Pico
uart = UART(0, baudrate=38400)

# Configuration des périphériques (LED RGB et moteur)
led_red = Pin(11, Pin.OUT)
led_green = Pin(12, Pin.OUT)
led_blue = Pin(13, Pin.OUT)
motor = Pin(14, Pin.OUT)

# Fonction pour envoyer des données
def send_data(data):
    uart.write(data + "\n")  # Ajout d'un saut de ligne pour marquer la fin des données

# Fonction pour recevoir des données
def receive_data():
    if uart.any():
        return uart.readline().decode('utf-8').strip()  # Décodage et suppression des espaces inutiles

# Fonction pour contrôler la LED RGB
def set_rgb_color(r, g, b):
    led_red.value(r)
    led_green.value(g)
    led_blue.value(b)

# Fonction pour contrôler le moteur
def control_motor(state):
    motor.value(state)

# Boucle principale
while True:
    # Réception des données Bluetooth
    incoming_data = receive_data()
    if incoming_data:
        print("Reçu :", incoming_data)
        
        # Analyse des commandes reçues
        if incoming_data == "BUTTON_PRESSED":
            # Allume la LED en rouge et démarre le moteur
            set_rgb_color(1, 0, 0)
            control_motor(1)
            send_data("LED ROUGE ET MOTEUR ON")
        elif incoming_data == "STOP":
            # Éteint la LED et arrête le moteur
            set_rgb_color(0, 0, 0)
            control_motor(0)
            send_data("LED OFF ET MOTEUR OFF")
        else:
            send_data("COMMANDE INCONNUE")

    # Pause pour éviter la saturation du buffer
    time.sleep(0.1)
