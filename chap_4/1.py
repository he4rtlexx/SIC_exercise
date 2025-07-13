from gpiozero import DistanceSensor,LED,Button
from datetime import datetime
from time import sleep

btn = Button(17)
led = LED(27)
led.off()
ultrasonic = DistanceSensor(echo=21, trigger=20)
span = 20

LOG_FILE = "/home/pi/Unit_Practice/distance_log.txt"

def log(distance):
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.now().strftime("%d-%m-%Y %SS:%MM:%HH")
        f.write(f"{timestamp}: {distance}%\n")
        f.close()

while True:
    distance = round(ultrasonic.distance*100, 3)
    print(distance)
    if btn.is_pressed:
        log(distance)

    if distance < 20:
        led.on()
    else:
        led.off()
    sleep(1)   
