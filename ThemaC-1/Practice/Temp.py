for i in range(200, 300):
    if pow(2, i - 1 ,i) == 1:
        print(i)

_ = [print(i) for i in range(200, 300) if pow(2, i - 1, i) == 1]