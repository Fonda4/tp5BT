from machine import UART
import time

# Configuration de l'UART sur le GPIO 0 (RX) et GPIO 1 (TX) pour le Pico
uart = UART(0, baudrate=38400)

# Fonction pour envoyer des données
def send_data(data):
    uart.write(data)
    print(len(data),data)

# Fonction pour recevoir des données
def receive_data():
    if uart.any():
        return uart.readline()
test = 0
# Exemple de boucle principale
while True:
    # Envoi de données à l'autre HC-05
    test += 1
    send_data(str(test))

    # Réception de données de l'autre HC-05
    incoming_data = receive_data()
    if incoming_data:
        print('Received:', incoming_data)

    # Pause pour éviter la saturation du buffer
    time.sleep(1)
