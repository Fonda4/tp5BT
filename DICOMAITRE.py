import ujson
from machine import UART, Pin
import time

# Initialiser l'UART (ajuste le numéro d'uart et les pins si besoin)
uart = UART(0, baudrate=38400)

def demander_et_envoyer():
    # Demande le type et la valeur à l'utilisateur
    type_objet = input("Entrez le type (ex: moteur) : ")
    valeur_str = input("Entrez la valeur (ex: 20) : ")
    
    try:
        # Tente de convertir en entier ou float selon le besoin
        if '.' in valeur_str:
            valeur = float(valeur_str)
        else:
            valeur = int(valeur_str)
    except ValueError:
        print("Valeur invalide, envoyée sous forme de chaîne.")
        valeur = valeur_str  # on l'envoie tel quel si ce n'est pas un nombre
    
    # Créer le dictionnaire
    data = {
        "type": type_objet,
        "valeur": valeur
    }
    
    # Convertir en JSON
    json_str = ujson.dumps(data)
    
    # Envoyer via UART (avec \n comme délimiteur)
    uart.write(json_str + "\n")
    print("Envoyé :", json_str)

# Boucle principale : envoie interactif
while True:
    demander_et_envoyer()
    time.sleep(0.5)  # petite pause avant de recommencer
