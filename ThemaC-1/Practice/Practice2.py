import re

num = input('数>')
while not re.fullmatch(r'^[1-9]+$', num):
    print('半角かつ、0以外の数字を入力してください.')
    num = input('数>')
else:
    num = int(num)

for i in range(1, num + 1):  # 段数
    print(i, ':', end='')
    for j in range(i):
        if not j == i-1:
            print('■', end='')
        else:
            print('■')