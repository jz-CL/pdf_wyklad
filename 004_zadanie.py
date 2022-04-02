# str. 54


"""
Stwórz funkcję, która sprawdzi, czy podany jako argument napis jest
palindromem (tj. czytany od przodu i wspak jest dokładnie taki sam, np.
„kajak”, „Madam”).



https://binarnie.pl/palindromy-implementacja-c/
"""


def is_palindrom(w):
    # usuń białe znaki, usuń wielkie litery

    w = w.lower().replace(" ", "")

    w_len = len(w)
    _ = w[0: w_len // 2]
    i = len(w) - 1
    for l in w[0: w_len // 2]:
        if l != w[i]:
            return False
        i -= 1

    return True


if __name__ == "__main__":
    _ = is_palindrom("Może jutro ta dama da tortu jeżom")
    print(_)
