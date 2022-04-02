# str. 55



"""
Stwórz funkcję, która obliczy liczbę małych i wielkich liter w ciągu.
np. dla : “The quick Brown Fox”

oczekiwany wynik :
Liczba wielkich liter : 3, liczba małych liter : 13

Podpowiedź: wykorzystaj pętlę, instrukcję warunkową i odpowiednie metody
dla stringa.


https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/
"""

def licz(litery):
    litery_wielkie = 0
    litery_male = 0

    for l in litery:
        if l.islower():
            litery_male += 1
        elif l.isupper():
            litery_wielkie += 1

    return litery_wielkie, litery_male

if __name__ == "__main__":
    litery_wielkie, litery_male = licz("The quick Brown Fox")
    print(f"Liczba wielkich liter : {litery_wielkie}, liczba małych liter : {litery_male}")
