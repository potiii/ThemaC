
price = int(input('金額(円)>'))
print('金額:', price, '円', sep='')

money_name = {10000: '一万円札=', 5000: '五千円札=', 1000: '千円札　=',
              500: '五百円玉=', 100: '百円玉　=', 50: '五十円玉=',
              10: '十円玉　=', 5: '五円玉　=', 1: '一円玉　='}

for item in money_name:
    print(money_name[item], price // item, '枚')
    price = price % item
