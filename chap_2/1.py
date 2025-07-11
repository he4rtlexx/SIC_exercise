from gpiozero import Button, LED
from time import sleep

btn = Button(17)
green = LED(27)
amber = LED(22)
red = LED(23)

led = [green, amber, red]
current = 0
led[current].on()

while True:
    if btn.is_pressed:
        led[current].off()
        current = (current + 1) % len(led)
        led[current].on()

        while btn.is_pressed:
            sleep(0.1)



