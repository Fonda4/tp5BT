from machine import UART, Pin, I2C
from ssd1306 import SSD1306_I2C
import time

# Configuration de l'UART sur le GPIO 4 (TX) et GPIO 5 (RX) pour le Pico
uart = UART(0, baudrate=38400)

# Configuration du bouton poussoir et de l'écran OLED
button = Pin(16, Pin.IN, Pin.PULL_UP)
i2c = I2C(0, scl=Pin(21), sda=Pin(20))
oled = SSD1306_I2C(128, 64, i2c)

# Fonction pour envoyer des données via Bluetooth
def send_data(data):
    uart.write(data + "\n")  # Ajout d'un saut de ligne pour marquer la fin des données

# Fonction pour recevoir des données via Bluetooth
def receive_data():
    if uart.any():
        return uart.readline().decode('utf-8').strip()

# Fonction pour afficher un message sur l'écran OLED
def display_message_ligne1(message):
    oled.fill(0)  # Efface l'écran
    oled.text(message, 0, 0)  # Affiche le message
    oled.show()
def display_message_ligne2(message1, message2):
    oled.fill(0)  # Efface l'écran
    oled.text(message1, 0, 0)  # Affiche le message
    oled.text(message2, 0, 20)  # Affiche le message
    oled.show()


bpressed = 0
mess1=""

# Boucle principale
while True:
    # Vérification de l'état du bouton poussoir
    if not button.value() and bpressed == 0:  # Si le bouton est pressé
        mess1 = "Button Pressed!"
        send_data("BUTTON_PRESSED")  # Envoie la commande au circuit esclave
        display_message_ligne1(mess1)
        bpressed=1
        time.sleep(0.5)  # Débounce (évite les multiples envois)
    elif button.value() and bpressed == 1:
        bpressed = 0
        send_data("STOP")
        mess1 = "STOP"
        display_message_ligne1(mess1)
    # Réception des données de l'esclave
    incoming_data = receive_data()
    if incoming_data:
        print("Recu :", incoming_data)
        display_message_ligne2(mess1, incoming_data)  # Affiche la réponse sur l'écran OLED

    # Pause pour éviter une surcharge
    time.sleep(0.5)
