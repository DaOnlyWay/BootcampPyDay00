import sys


def rev_alpha(listargv):
    str = ""
    for i in reversed(range(len(listargv))):
        if i != 0:
            str += listargv[i][::-1]
        if i > 1:
            str += " "
    print(str.swapcase())


rev_alpha(sys.argv)
