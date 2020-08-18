import time

from datetime import datetime
from picamera import PiCamera

camera = PiCamera()

now_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
camera.preview()
for i in range(18):
    camera.resolution = (320, 240)
    camera.image_effect = 'emboss'
    camera.annotate_text = now_time
    camera.capture('pic2/image{0}.jpg'.format(i))
    time.sleep(10)
camera.stop_preview()
