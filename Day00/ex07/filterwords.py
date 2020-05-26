import sys
import string


def filterwords(args):
    if len(args) > 3 or args[2].isdigit() == 0 or len(args) < 3:
        print("ERROR")
        return
    temp = args[1].translate(str.maketrans('', '', string.punctuation))
    list = temp.split()
    final_list = []
    print(list)
    wc = int(args[2])
    for i in list:
        if len(i) > wc:
            final_list.append(i)
    print(final_list)


filterwords(sys.argv)
