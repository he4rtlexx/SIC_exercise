from datetime import datetime
from gpiozero import LED
import psutil
from time import sleep

red = LED(23)
yellow = LED(22)

LOG_FILE = "/home/pi/Unit_Practice/disk_usage_log.txt"

def log(disk_usage):
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.now().strftime("%d-%m-%Y %SS:%MM:%HH")
        f.write(f"{timestamp}: {disk_usage}%\n")
        f.close()

while True:
    disk_usage = psutil.disk_usage("/").percent
    if disk_usage > 60:
        red.on()
        yellow.off()
    elif 30 <= disk_usage <= 60:
        red.off()
        yellow.on()
    else:
        red.off()
        yellow.off()
    log(disk_usage)
    
    sleep(5)


