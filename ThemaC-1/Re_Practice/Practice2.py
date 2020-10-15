num = int(input('数>'))

for i in range(1, num +1):
    print(i,':',end='')
    for j in range(i):
        if not j == i-1:
            print('■', end='')
        else:
            print('■')