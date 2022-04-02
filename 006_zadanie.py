# str. 56



"""
Napisz funkcję, która przyjmuje dwa stringi i sprawdza, czy są swoimi
anagramami.

Na przykład:

„army” i „Mary”,
„dzielenia” i „niedziela”,
„Quid est veritas?” i „Vir est qui adest”,
„Jim Morrison” i „Mr Mojo Risin”
„Tom Marvolo Riddle” i „I am Lord Voldemort”


https://wordlist.eu/anagramy
https://www.geeksforgeeks.org/python-sorted-check-two-strings-anagram-not/
"""


def anagram(fraza1, fraza2):
    fr1 = fraza1.lower().replace(" ", "")
    fr2 = fraza2.lower().replace(" ", "")

    if sorted(fr1) == sorted(fr2):
        print("wybrane słowa są anagramem")
    else:
        print("wybrane słowa nie są anagramem")



if __name__ == "__main__":
    anagram("army", "Mary")
    
