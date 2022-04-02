# str. 146
"""
Napisz program, który zwróci wartość bezwzględną liczby pobranej od
użytkownika. Program powinien pytać o tę liczbę tak długo, aż nie zostanie
ona poprawnie podana.
Pamiętaj, że użytkownik nie zawsze wpisze wartość numeryczną, może
też wpisać np. “kalafior”. Sprawdź, co wtedy się stanie i pamiętaj o obsłudze
wyjątków.

"""
# import math
import sys

if __name__ == "__main__":
    xx = sys.argv
    exit_loop = False
    while not exit_loop:

        liczba = input("podaj liczbę ")
        try:
            liczba = float(liczba)
            liczba = abs(liczba)
            exit_loop = not exit_loop
        except TypeError:
            print("Ponownie podaj wartość...")
        except ValueError:
            print("Ponownie podaj wartość...")

    print(f"wartość bezwględna z podane danej {abs(liczba)}")