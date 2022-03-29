from gpiozero import LED
from time import sleep

led = LED(4)  #GPIO4

for i in range(5):  
    print("LED ON")
    led.on()
    sleep(1)
    print("LED OFF")
    led.off()
    sleep(1)




