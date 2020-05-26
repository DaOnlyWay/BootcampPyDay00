def kata03():
    str = "The right format"
    fill = 42 - len(str) - 1
    for i in range(fill):
        print('-', end='')
    print(str)


kata03()
