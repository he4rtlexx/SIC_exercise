from gpiozero import LED

led_1 = LED(27)
led_2 = LED(22)

while True:
    s = input()
    match s:
        case "1 ON":
            led_1.on()
        case "1 OFF":
            led_1.off()
        case "2 ON":
            led_2.on()
        case "2 OFF":
            led_2.off()
        case _:
            print("Invalid command!!!")
