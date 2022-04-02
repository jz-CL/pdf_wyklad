# str. 50

"""
Napisz program, który zamieni wprowadzony przez użytkownika ciąg cyfr na
formę tekstową, np.:
112 - > „jeden jeden dwa”
9973 -> „dziewięć dziewięć siedem trzy”
Podpowiedź: potrzebujesz funkcji input(), słownika oraz pętli.

"""


def digit_to_word(digit):
    word = {
        "1": "jeden",
        "2": "dwa",
        "3": "trzy",
        "4": "cztery",
        "5": "pięć",
        "6": "sześć",
        "7": "siedem",
        "8": "osiem",
        "9": "dziewięć",
        "0": "zero",
    }

    return word[str(digit)]


def digits(liczba):
    liczba_split = list(liczba)
    word = ""

    for _ in liczba_split:
        w = digit_to_word(_)
        word += w + " "

    return word[0: len(word) - 1]


if __name__ == "__main__":
    print(digits("112"))
    print(digits("9973"))
