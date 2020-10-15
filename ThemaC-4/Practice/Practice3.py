import time

from datetime import datetime
from picamera import PiCamera

camera = PiCamera()  # 定義

now_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
# Practice2の同じやつとやってることは同じ
camera.preview()  # カメラの起動
for i in range(18):  # これも同じ
    camera.resolution = (320, 240)  # 写真の解像度を320*240に指定
    camera.image_effect = 'emboss'  # エンボス加工に指定
    camera.annotate_text = now_time  # これも同じ
    camera.capture('pic2/image{0}.jpg'.format(i))  # これも同じ
    time.sleep(10)  # 10秒待つ
camera.stop_preview()  # カメラの終了
