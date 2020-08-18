import time

from datetime import datetime
from picamera import PiCamera

now_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

camera = PiCamera()
camera.start_preview()

for i in range(18):
    camera.annotate_text = now_time
    camera.capture('pic2/image{0}.jpg'.format(i))
    time.sleep(10)
camera.stop_preview()
