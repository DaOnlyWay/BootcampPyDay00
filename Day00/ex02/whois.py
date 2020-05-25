import sys


def whois(listarg):
    num = listarg[1]
    if len(listarg) > 2:
        print("ERROR")
    elif num.isnumeric() == 0:
        print("ERROR")
    elif int(num) == 0:
        print("I'm Zero.")
    elif (int(num) % 2) == 0:
        print("I'm Even.")
    elif (int(num) % 2) != 0:
        print("I'm odd.")


whois(sys.argv)
