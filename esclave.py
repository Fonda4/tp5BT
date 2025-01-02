import uasyncio as asyncio
from machine import UART, Pin, PWM
from dcmotor import DCMotor

class BluetoothHC05:
    def __init__(self, tx_pin, rx_pin, led_pin_R, led_pin_G, led_pin_B, motor_pins, pwm_pin, frequency=30000, baudrate_=38400):
        # UART Configuration
        self.uart = UART(0, baudrate=baudrate_)
        # LED Configuration
        self.led_R = Pin(led_pin_R, Pin.OUT)
        self.led_G = Pin(led_pin_G, Pin.OUT)
        self.led_B = Pin(led_pin_B, Pin.OUT)
        # DC Motor Configuration
        self.motor_pin1 = Pin(motor_pins[0], Pin.OUT)
        self.motor_pin2 = Pin(motor_pins[1], Pin.OUT)
        self.enable = PWM(Pin(pwm_pin), freq=frequency)
        self.dc_motor = DCMotor(self.motor_pin1, self.motor_pin2, self.enable, frequency)

    def set_rgb_color(self, r, g, b):
        self.led_R.value(r)
        self.led_G.value(g)
        self.led_B.value(b)

    def control_motor(self, speed):
        if speed > 0:
            self.dc_motor.forward(speed)
        else:
            self.dc_motor.stop()

    async def send_data(self, data):
        message = data + "\n"
        self.uart.write(message)
        await asyncio.sleep(0)

    async def receive_data(self):
        while True:
            if self.uart.any():
                message = self.uart.read()
                await asyncio.sleep(0)
                return message.decode('utf-8').strip()
            await asyncio.sleep(0)

    async def process_command(self, command):
        
        if command == "BUTTON_PRESSED":
            # Allume la LED en rouge et démarre le moteur à 100 %
            self.set_rgb_color(1, 0, 0)
            self.control_motor(100)
            await self.send_data("LED RED \n MOTEUR ON ")
            print("Moteur ON à 100%")
        elif command == "STOP":
            # Éteint la LED et arrête le moteur
            self.set_rgb_color(0, 0, 0)
            self.control_motor(0)
            await self.send_data("LED OFF \n MOTEUR OFF")
            print("Moteur OFF")
        else:
            await self.send_data("COMMANDE INCONNUE")

    async def listen(self):
        while True:
            data = await self.receive_data()
            if data:
                await self.process_command(data)

# Exemple d'utilisation de la classe avec asyncio
async def main():
    bluetooth = BluetoothHC05(
        tx_pin=0, 
        rx_pin=1, 
        led_pin_R=11, 
        led_pin_G=12, 
        led_pin_B=13, 
        motor_pins=(6, 7), 
        pwm_pin=8
    )

    asyncio.create_task(bluetooth.listen())  # Coroutine pour écouter les données entrantes

    while True:
        await asyncio.sleep(1)

# Démarrage de la boucle d'événements asyncio
asyncio.run(main())
