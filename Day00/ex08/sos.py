import sys

morse_dico = {
              'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
              'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
              'Z': '--..', '1': '.---', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.', '10': '-----'
             }

sys.argv.pop(0)


def sos(list):
    code = ''
    for words in list:
        upwords = words.upper()
        for letter in upwords:
            if letter != ' ':
                if letter.isalnum() == 0:
                    print("ERROR")
                    return
                code += morse_dico[letter] + ' '
            elif upwords[-1] != ' ':
                code += '/ '
        if words != list[-1]:
            code += '/ '
    print(code)


sos(sys.argv)
