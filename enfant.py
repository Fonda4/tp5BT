import uasyncio as asyncio
from machine import UART, Pin
from dcmotor import DCMotor

class BluetoothHC05:
    def __init__(self, tx_pin, rx_pin, led_pin_R,led_pin_G,led_pin_B, motor_pin_1,motor_pin_2, baudrate_=38400):
        self.uart = UART(0, baudrate=baudrate_) #, tx=tx_pin, rx=rx_pin)
        self.led_R = Pin(led_pin_R, Pin.OUT)
        self.led_G = Pin(led_pin_G, Pin.OUT)
        self.led_B = Pin(led_pin_B, Pin.OUT)
        self.motor_1 = Pin(motor_pin_1, Pin.OUT)
        self.motor_2 = Pin(motor_pin_2, Pin.OUT)

        print("UART lancé")

    def set_rgb_color(self,r, g, b):
        self.led_R.value(r)
        self.led_G.value(g)
        self.led_B.value(b)

    def control_motor(self,state):
        self.motor.value(state)

    async def send_data(self, data):
        message = data + "\n"
        self.uart.write(message)
        await asyncio. sleep(0)

    async def receive_data(self):
        while True:
            if self.uart.any():
                #print ("data recu")
                message =  self.uart.read()  #await
                await asyncio.sleep(0)
                message = message.decode('utf-8').strip()
                #print ( message )
                return message
            
                """
                message = await self.uart.read()
                if message.startswith(b'START:') and message.endswith(b':END\n'):
                    return message[6:-5]
                """
            await asyncio.sleep(0)

    async def process_command(self, command):
        print(command)
        if command == "BUTTON_PRESSED":
            # Allume la LED en rouge et démarre le moteur
            self.set_rgb_color(1, 0, 0)
            self.control_motor(1)
            # print("LED turned ON")
            await self.send_data("LED RED ET MOTEUR ON")
            print("LED turned ON")
        elif command == "STOP":
            # Éteint la LED et arrête le moteur
            self.set_rgb_color(0, 0, 0)
            self.control_motor(0)
            await self.send_data("LED ET MOTEUR OFF")
        else:
            await self.send_data("COMMANDE INCONNUE")

    async def listen(self):
        while True:
            print("boucle listner")
            data =  await self.receive_data()
            if data:
                print(" process command ", data)
                await self.process_command(data)

# Exemple d'utilisation de la classe avec asyncio
async def main():
    # Remplacez 'tx_pin', 'rx_pin', 'led_pin' et 'motor_pin' par les numéros de broches GPIO appropriés
    bluetooth = BluetoothHC05(tx_pin=0, rx_pin=1, led_pin_R=11,led_pin_G=12,led_pin_B=13,motor_pin=6)

    asyncio.create_task(bluetooth.listen())  # Coroutine pour écouter les données entrantes

    print("thread lancé")
    while True:
        # Ici, vous pourriez ajouter des tâches périodiques ou des commandes
        await asyncio.sleep(1)

# Démarrage de la boucle d'événements asyncio
asyncio.run(main())
