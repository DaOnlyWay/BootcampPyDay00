def kata00():
    t = 19, 42, 21, 42, 24
    ln = len(t)
    print("The", ln, "numbers are: ", end='')
    for i in range(len(t)):
        print(t[i], end='',)
        if i != ln - 1:
            print(", ", end='',)


kata00()
