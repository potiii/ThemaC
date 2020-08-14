from datetime import datetime
import time
from picamera import PiCamera

camera = PiCamera()
camera.start_preview()
for i in range(18):
    camera.annotate_text=datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    camera.capture('pic2/image%s.jpg' % i)
    time.sleep(10)
camera.stop_preview()
