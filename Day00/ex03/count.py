import string


def text_analyzer(str):
    upper = 0
    lower = 0
    space = 0
    ponct = 0
    punctuation = string.punctuation
    for i in str:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i == ' ':
            space += 1
        elif i in punctuation:
            ponct += 1
    total = upper + lower + space + ponct
    print("The text contains" ,total, "characters:")
    print("\n-" ,upper, "upper letters")
    print("\n-" ,lower, "lower letters")
    print("\n-" ,ponct, "punctuation marks")
    print("\n-" ,space, "spaces")
