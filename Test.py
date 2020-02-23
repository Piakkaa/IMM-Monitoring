import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
sensor = 16
elapse = 0.00
short_no = 0.00

start = time.time()

GPIO.setup(sensor, GPIO.IN, pull_up_down = GPIO.PUD_UP)
def get_elapse():
    return elapse

def get_short_no():
    return short_no

def get_pulse(number):
    global elapse,pulse,short_no
    cycle = 0
    pulse+=1
    cycle+=1
    if pulse > 0:
        elapse = time.time() - start
        pulse -=1

    short_no = cycle
    start = time.time()



try:

    time.sleep(1)

    GPIO.add_event_detect(sensor,GPIO.FALLING,callback = get_pulse,bouncetime=25)
    while True:
        print('short_no:{0:.0f} elapse:{1:.4f}'.format(short_no,elapse))
        time.sleep(0.1) #to reduce CPU load, print every 100 milliseconds


except KeyboardInterrupt:
    print('You have pressed Ctrl+C! How dare you stopped this beautiful thing?!')
    GPIO.cleanup()
