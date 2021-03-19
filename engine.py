import RPi.GPIO as GPIO
import time

servoPIN = 4
enginePIN = 14

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(enginePIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
p.start(2.5) # Initialisierung
GPIO.output(enginePIN, 0)

def duty(angle):
    return angle / 18 + 2

def finish():
    p.stop()
    GPIO.output(enginePIN, 0)
    GPIO.cleanup()

try:
    p.ChangeDutyCycle(duty(30))
    time.sleep(2)
    p.ChangeDutyCycle(duty(130))
    time.sleep(2)
    GPIO.output(enginePIN, 1)
    time.sleep(10)
    finish()
        
except KeyboardInterrupt:
    finish()