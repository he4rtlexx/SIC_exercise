from gpiozero import Button, LED
from signal import pause

btn = Button(17)
green = LED(27)
amber = LED(22)
red = LED(23)

led = [green, amber, red]
current = 0
led[current].on()

def cycle_led():
    global current
    led[current].off()
    current = (current + 1) % len(led)
    led[current].on()

btn.when_pressed = cycle_led

pause()
