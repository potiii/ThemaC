import time

import datetime

import dht11
import RPi.GPIO as GPIO


class Dht_run:
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()

        self.instance = dht11.DHT11(pin=14)

    def csv_write(self):
        path_w = 'Practice4.csv'
        with open(path_w, mode='w') as file:
            for i in range(300):
                result = self.instance.read()
                now = str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
                temp = str(result.temperature)
                rh = str(result.humidity)
                if result.is_valid():
                    file.write(
                        now + str(',') + temp + ',' + rh + '\n')
                time.sleep(1)


def main():
    dht = Dht_run()
    dht.csv_write()


if __name__ == '__main__':
    main()
