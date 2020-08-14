import RPi.GPIO as GPIO
import dht11
import time
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin=14)

path_w = 'Practice4.csv'
with open(path_w, mode='w') as f:
    for i in range(300):
        result = instance.read()
        if result.is_valid():
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: %d C" % result.temperature)
            print("Humidity: %d %%" % result.humidity)
            f.write(
                str(datetime.datetime.now()) + str(',') + str(result.temperature) + ',' + str(result.humidity) + '\n')

        time.sleep(1)
