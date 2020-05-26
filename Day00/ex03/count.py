import string


def text_count(txt):
    upper = 0
    lower = 0
    space = 0
    ponct = 0
    punctuation = string.punctuation
    for i in txt:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i == ' ':
            space += 1
        elif i in punctuation:
            ponct += 1
    print("The text contains", len(txt), "characters:")
    print("\n-", upper, "upper letters")
    print("\n-", lower, "lower letters")
    print("\n-", ponct, "punctuation marks")
    print("\n-", space, "spaces")


def text_analyzer(*args):
    if len(args) > 1:
        print("ERROR")
    elif len(args) == 0:
        line = input("What is the text to analyse?\n")
        text_count(line)
    elif len(args) == 1:
        text_count(args[0])
