#https://www.youtube.com/watch?v=U6N5pRDOrg4

import RPi.GPIO as GPIO
import time

pin=4  #GPIO4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #boton

for i in range(5):   
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(.1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(.1)
GPIO.cleanup()


led_on = False

def switch():
  global led_on
  led_on = not led_on
  GPIO.output(pin, GPIO.HIGH if led_on else GPIO.LOW)

GPIO.add_event_detect(23, GPIO.FALLING, callback=switch, bouncetime=300)
#GPIO.add_event_detect(23, GPIO.RISING, callback=switch, bouncetime=300)
