import time

import datetime

import dht11
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
# 上3行はおまじないみたいなものだから特に気にしなくていい

instance = dht11.DHT11(pin=14)
# pin14のDHT11センサーを起動

path_w = 'Practice4.csv'
# ここでファイル名を指定

with open(path_w, mode='w') as file:
    # with openで開くと勝手に使い終わったらファイルを閉じてくれる
    # ここでas fileって指定してあげると後でopen(path_w, mode='w')って記述しなきゃいけないときにfileって記述するだけで済む
    # with open(ファイル名, mode='w'[writeのこと mode='r'ってすると読み取り専用モードになる]) as 変数:

    for i in range(300):  # 5min = 300sec
        result = instance.read()
        # 13行目で起動したセンサーの内容を読み取って変数に保存

        now = str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
        # CSVに保存するための日時データをstring型で保存する
        # datetimeはdatetime型でしか取れないから、そのままだと保存するときにエラーが出る

        temp = str(result.temperature)
        # DHT11で取得した温度データをString型に変換して変数に保存

        rh = str(result.humidity)
        # DHT11で取得した湿度データをString型に変換して変数に保存

        if result.is_valid():
            # resultにデータがあるかを確認

            file.write(
                # open(path_w, mode='w').writeとやってることは同じ

                now + str(',') + temp + ',' + rh + '\n')
            # CSVに書き込むデータの生成
            # 2020/01/01 12:00:00,22.5,60.2\n みたいな感じで書き込まれる 最後の\nを忘れるとデータがバグる

        time.sleep(1)  # 1秒待つ
