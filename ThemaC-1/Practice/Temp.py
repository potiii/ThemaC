price = input()

money1 = ['一万円札', '五千円札', '千円札', '五百円玉', '百円玉', '五十円玉', '十円玉', '五円玉', '一円玉']
money2 = [10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

for item in range(9):
    print(money1[item], int(price) // money2[item], '枚')
    price = int(price) % money2[item]
