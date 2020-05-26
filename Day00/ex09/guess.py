import random


def guess():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 ", end='')
    print("to find out the secret number.")
    print("Type exit to end the game")
    randval = random.randint(1, 99)
    count = 0
    value = ''
    while value != 'exit':
        value = input("What's your guess between 1 and 99 ?")
        if int(value) > randval:
            print("Too high!")
            count += 1
        elif int(value) < randval:
            print("Too low!")
            count += 1
        elif int(value) == randval:
            if randval == 42:
                print("The answer to the ultimate quesion of life, ", end='')
                print("the universe and everything is 42")
            if count == 0:
                print("Congratulation! You've got it on your first try!")
            else:
                print("Congratulation, you've got it")
                print("You won in %d attempts!" % count)
            return
        elif value == "exit":
            print("Goodbye!")
            return


guess()
