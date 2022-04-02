# str. 63


"""
Napisz funkcję, która zwróci 5 najczęstszych słów z dzieła Mickiewicza.
https://pastebin.com/raw/aAHeW5Pt (przekopiuj i zapisz do pliku tekstowego
to, co znajdziesz pod tym linkiem).

Podpowiedź: skorzystaj z funkcji open(), metody split(), słownika oraz pętli.

https://oprojektowaniu.pl/python-dla-inzynierow-slowniki/

"""

slownik = {}
DIR = "./"


def dodaj_slowo(word):
    if slownik.get(word, -1) != -1:
        # jest słowo
        wartosc = slownik[word]
        slownik[word] = wartosc + 1
    else:
        slownik[word] = 1


def czytaj_plik():
    f = open(DIR + "/" + "text.txt")
    slowo = f.read().split()
    f.close()
    return slowo


if __name__ == "__main__":
    words = czytaj_plik()
    for w in words:
        dodaj_slowo(w.lower())

    sort_slowniks = sorted(slownik.items(), key=lambda x: x[1], reverse=True)
    print(sort_slowniks[0:5])
