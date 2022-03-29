import RPi.GPIO as GPIO
import time

pin=7  #GPIO3

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.OUT)

# while True:
for i in range(0,5):   #ejecuta 5 veces
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.5)
GPIO.cleanup()