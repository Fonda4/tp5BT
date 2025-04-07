# A2071 - Robotique (Part 1) - 2024-2025



## *Projet: Mini Robot Télécommandé*

Binôme (B1)
- Xu Keng HE305064
- Fondimare Nathan HE304827
- de Meeus Justin HE304831
- Foyet Fondjo David HE305102

### Objectifs:
<!---0------------------------------------------------------>
<!---------------------------------------------------------->

<details>
<summary>0. Objectif du projet</summary>

- Concevoir, construire et programmer un robot mobile radiocommandé.
- Le robot devra effectuer des mouvements, éviter des obstacles et exécuter des tâches simples.


</details>


<!--------------1------------------------------------------->
<!---------------------------------------------------------->

<details>
<summary>1. Cadre du projet</summary>

- Réalisé par des étudiants durant le deuxième quadrimestre.
- Travail en classe (séances présentielles) et à domicile.
- Acquisition de compétences en :
  - Conception mécanique
  - Électronique
  - Programmation
  - Automatisation

</details>


<!---2------------------------------------------------------>
<!---------------------------------------------------------->

<details>
<summary>2. Modes de fonctionnement du robot</summary>

- Mode manuel
    - Contrôle à distance via une télécommande.

- Mode autonome
    - Détection et évitement des obstacles grâce à des capteurs embarqués.
    - Mise en œuvre d’algorithmes d’évitement intelligents.
</details>

<!--- TESTS------------------------------------------------->
<!---------------------------------------------------------->

<details>
<summary>3. Finalité pédagogique</summary>

- Exploration des principes de télécommande et d’automatisation.
- Compréhension approfondie des concepts de robotique et d’intelligence embarquée.
- Définition des spécifications et fonctionnalités en fonction des deux modes de fonctionnement.

</details>


<!--- CONTROLES--------------------------------------------->
<!---------------------------------------------------------->


<details>
<summary>4. Sources</summary>


SparkFun Electronics. HC-SR04 Ultrasonic Sensor Datasheet. Auteur inconnu. [PDF en ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf
```
Wikipédia. Ultrason. [En ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://fr.wikipedia.org/wiki/Ultrason
```
Ducros, Christian. Les 3 raisons de la programmation asynchrone. [Vidéo en ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://www.youtube.com/watch?v=GzPktikU_PI
```
Ducros, Christian. Programmation asynchrone partie 1/4 module uasyncio. [Vidéo en ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://www.youtube.com/watch?v=xe_OZ6WnSY4
```
Ducros, Christian. Programmation asynchrone partie 2/4 module uasyncio. [Vidéo en ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://www.youtube.com/watch?v=xe_OZ6WnSY4
```

Ducros, Christian. Programmation asynchrone partie 3/4 module uasyncio. [Vidéo en ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://www.youtube.com/watch?v=UptaQVDQeRg
```

Ducros, Christian. Programmation asynchrone partie 4/4 module uasyncio. [Vidéo en ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://www.youtube.com/watch?v=DCvGdwg1Iiw
```

christianDUCROS. GitHub - christianDUCROS/uasyncio : exemples. [En ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://github.com/christianDUCROS/uasyncio
```

Instructables Workshop. Understanding the basics of electricity. [PDF en ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://content.instructables.com/F8O/SMME/IU5NM2JJ/F8OSMMEIU5NM2JJ.pdf
```

Compuphase. Termite. [En ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://www.compuphase.com/software_termite.htm
```
SourceForge. Y-A Terminal. [En ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://sourceforge.net/projects/y-a-terminal/
```

MicroPython Development Team. _thread — Multi-threading support. [En ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://docs.micropython.org/en/latest/library/_thread.html
```

MicroPython Development Team. asyncio — Asynchronous I/O support. [En ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://docs.micropython.org/en/latest/library/asyncio.html
```

ElectroSoftCloud. Script multithreadé sur Raspberry Pi Pico et MicroPython. [En ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://www.electrosoftcloud.com/en/multithreaded-script-on-raspberry-pi-pico-and-micropython/
```

DigiKey. (2021, 9 août). How to Use Asyncio in MicroPython (Raspberry Pi Pico) [Vidéo en ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://www.youtube.com/watch?v=5VLvmA__2v0
```

MicroPython. (2023, 3 juin). MicroPython Meetup May 2023. ASYNCIO Profiler demonstration [Vidéo en ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://www.youtube.com/watch?v=qQ-t11hHWXQ
```

class Pin – control I/O pins — MicroPython latest documentation. (s. d.). [En ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://docs.micropython.org/en/latest/library/machine.Pin.html#machine-pin
```

class Timer – control hardware timers — MicroPython latest documentation. (s. d.). [En ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://docs.micropython.org/en/latest/library/machine.Timer.html
```

Quick reference for the RP2 — MicroPython latest documentation. (s. d.). [En ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://docs.micropython.org/en/latest/rp2/quickref.html#pwm-pulse-width-modulation
```

Peppe8o. ssd1306.py. [En ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://peppe8o.com/download/micropython/ssd1306/ssd1306.py
```

Santos, S., & Santos, S. (2023, 5 juillet). MicroPython : OLED Display with ESP32 and ESP8266 | Random Nerd Tutorials. [En ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://randomnerdtutorials.com/micropython-oled-display-esp32-esp8266/
```
Das, A. (2024, 24 mai). Raspberry Pi Pico Interrupts Tutorial- Examples in MicroPython. [En ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://electrocredible.com/raspberry-pi-pico-external-interrupts-button-microp ython/
```

Voici vos références reformatées de façon plus lisible :
Moteurs électriques pour la robotique. (2025, 6 janvier). [En ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://www.dunod.com/sciences-techniques/moteurs-electriques-pour-robotique-0
```
Texas Instruments. (s.d.). L293. [En ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://www.ti.com/lit/ds/symlink/l293.pdf
```
Pont-H L293D — MCHobby - Wiki. (s.d.). [En ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://wiki.mchobby.be/index.php?title=Pont-H_L293D
```
STMicroelectronics. (s.d.). L298. [En ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://www.mouser.be/datasheet/2/389/l298-1849437.pdf
```
Pont-H L298N — MCHobby - Wiki. (s.d.). [En ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://wiki.mchobby.be/index.php?title=Pont-H_L298N
```
Eskimon. (s.d.). Un moteur qui a de la tête : le Servomoteur - Arduino : premiers pas en informatique embarquée. [En ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://zestedesavoir.com/tutoriels/686/arduino-premiers-pas-en-informatique-embarquee/747_le-mouvement-grace-aux-moteurs/3438_un-moteur-qui-a-de-la-tete-le-servomoteur/
```
PICO Servo Driver - MakerFabs Wiki. (s.d.). [En ligne]. Disponible sur : (consulté le 6 janvier 2025).
```
https://wiki.makerfabs.com/PICO_Servo_Driver.html
```





** **

</details>

<!---------------------------------------------------------->





