import pandas
from matplotlib import pyplot

df = pandas.read_csv('Practice4.csv', names=['time', 'temperature', 'humidity'])
# pandas.read_csv(ファイル名, names=[CSV内の情報])
# 今回は中のデータが2020/01/01 12:00:00,22.5,60.2みたいな形だから、上みたいな形でパースしてあげるといい感じになる

fig, ax1 = pyplot.subplots()
# 定義

ax1.plot(df['temperature'], color='red')
# わかりやすいように温度を赤色で表示

ax2 = ax1.twinx()
# ax2(湿度)をax1(温度)と関連付け

ax2.plot(df['humidity'])
# デフォルトで青色だから湿度はそのまま

pyplot.show()
# プロットしたグラフを表示する

fig.savefig('img.png')
# プロットしたグラフを保存する

# 考えるの嫌になって適当に生成したからもっと適切なグラフはある　とりあえず作るだけ作るためのやつだから点数取れるかは知らん
