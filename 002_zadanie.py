# str. 51

"""
Stwórz funkcję przyjmującą listę liczb całkowitych, a zwracającą informację,
na której pozycji znajduje się najmniejsza liczba.
Nie korzystaj z wbudowanych funkcji.
np. dla listy [42, 13, 56, 7, 12, 3, 85] funkcja powinna zwrócić 5, ponieważ pod
tym indeksem w tej liście znajduje się element najmniejszy.
"""


def funkcja(liczba):
    next_element = 0

    j_min = l[next_element]
    j_index = next_element

    for j in liczba[1:]:
        next_element += 1
        if j < j_min:
            j_min = j
            j_index = next_element

    return j_index


if __name__ == "__main__":
    i = funkcja([42, 13, 56, 7, 12, 3, 85])
    print(i)
