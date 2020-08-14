from datetime import datetime
import time
from picamera import PiCamera

camera = PiCamera()
camera.start_preview()
for i in range(18):
    camera.resolution = (320,240)
    camera.image_effect = 'emboss'
    camera.annotate_text=datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    camera.capture('pic2/image%s.jpg' % i)
    time.sleep(10)
camera.stop_preview()
