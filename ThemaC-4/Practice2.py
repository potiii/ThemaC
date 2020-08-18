import time

from datetime import datetime
from picamera import PiCamera

now_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
# datetime.now()で現在時刻を取得する 取得した段階では 2020-01-01 12:00:00.999999 みたいな形でミリ秒まで入ってる
# .strftime("%Y/%m/%d %H:%M:%S")では、そのデータを2020/01/01 12:00:00みたいな形にフォーマットする

camera = PiCamera()  # 定義
camera.start_preview()  # カメラの起動

for i in range(18):
    # Javaで言うと for (int i = 0; i < 18; i++) 18回繰り返す
    camera.annotate_text = now_time
    # 画像に文字を印字する now_timeは6行目で取得した時間のこと now_timeを任意の文字に変えるとそれになる
    camera.capture('pic2/image{0}.jpg'.format(i))
    # 画像を撮影・保存する ディレクトリ名とファイル名を指定する
    # {0}はformat関数で、文字列以降の.formatの中で指定した変数を代入するもの
    # 今回の場合はファイル名が被ると結果が出力されないので、iを代入して対応する
    # i=0のときはimage0.jpg,i=1のときはimage1.jpgみたいになる
    time.sleep(10)  # 10秒待つ

camera.stop_preview()  # カメラの終了
