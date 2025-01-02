import uasyncio as asyncio
from machine import UART, Pin

class BluetoothHC05:
    def __init__(self, tx_pin, rx_pin, led_pin, motor_pin, baudrate=9600):
        self.uart = UART(0, baudrate=baudrate, tx=tx_pin, rx=rx_pin)
        self.led = Pin(led_pin, Pin.OUT)
        self.motor = Pin(motor_pin, Pin.OUT)

    async def send_data(self, data):
        message = "START:{}:END\n".format(data)
        self.uart.write(message)
        await asyncio.sleep(0)

    async def receive_data(self):
        while True:
            if self.uart.any():
                message = await self.uart.read()
                if message.startswith(b'START:') and message.endswith(b':END\n'):
                    return message[6:-5]
            await asyncio.sleep(0)

    async def listen(self):
        while True:
            data = await self.receive_data()
            if data:
                self.process_command(data.decode())

    def process_command(self, command):
        if command == "LED_ON":
            self.led.value(1)
            print("LED turned ON")
        elif command == "LED_OFF":
            self.led.value(0)
            print("LED turned OFF")
        elif command == "MOTOR_START":
            self.motor.value(1)
            print("Motor started")
        elif command == "MOTOR_STOP":
            self.motor.value(0)
            print("Motor stopped")
        else:
            print("Unknown command:", command)

# Exemple d'utilisation de la classe avec asyncio
async def main():
    # Remplacez 'tx_pin', 'rx_pin', 'led_pin' et 'motor_pin' par les numéros de broches GPIO appropriés
    bluetooth = BluetoothHC05(tx_pin=1, rx_pin=0, led_pin=2, motor_pin=3)

    asyncio.create_task(bluetooth.listen())  # Coroutine pour écouter les données entrantes

    while True:
        # Ici, vous pourriez ajouter des tâches périodiques ou des commandes
        await asyncio.sleep(1)

# Démarrage de la boucle d'événements asyncio
asyncio.run(main())
