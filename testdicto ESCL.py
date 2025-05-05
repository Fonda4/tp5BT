import ujson
from machine import UART, Pin

uart = UART(0, baudrate=38400)

buffer = b""

while True:
    if uart.any():
        # Lire tout ce qui est disponible
        buffer += uart.read()
        
        # Découper par ligne si tu as utilisé \n comme séparateur
        if b"\n" in buffer:
            ligne, buffer = buffer.split(b"\n", 1)
            try:
                # Convertir depuis JSON vers dictionnaire
                data = ujson.loads(ligne)
                print("Reçu :", data)
            except Exception as e:
                print("Erreur de décodage :", e)
