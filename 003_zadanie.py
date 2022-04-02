# str. 52

"""
Stwórz funkcję, która sprawdzi, czy liczba podana w argumencie jest pierwsza.
Funkcja powinna przyjmować wartość numeryczną, a zwracać powinna
wartość logiczną True/False.
Np.
Dla 11 funkcja zwróci True, natomiast dla 12 -> False.

https://python.oeiizk.waw.pl/strony/interaktywne2/25_sito.html

"""


def liczba_pierwsza(liczba):
    for licz in range(2, liczba):
        if liczba % licz:
            return False
    return True


if __name__ == "__main__":
    lp = liczba_pierwsza(12)
    print(lp)
