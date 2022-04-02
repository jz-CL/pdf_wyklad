# str. 125

# dekorator jako jedyny argument przyjmuje funkcję którą ma udekorować
# przyjmuje funkcję jako swój argument
def my_decorator(func):
    # definiuje wewnętrzną funkcję -> wraper -> wykonuje funkcję którą dekorujemy, wykonuje też dodatkową czynność
    #  w typ przykładzie dopisuje dodatkowe napisy przed i po wyniku funkcji
    def wrapper():
        # zwraca funkcję jako wynik swojego działania
        # oraz dodatkowe działanie
        return f"DECORATED -> {func()} <- DECORATED"

    #  zwraca wrapper jako swój wynik
    return wrapper



def hello_world():
    return f"Hello, world!"


print(hello_world())
# Hello, world!

print(my_decorator(hello_world)())
# DECORATED -> Hello, world! <- DECORATED

'''
po zastosowaniu dekoratora -> zwraca on oryginalną funkcję owiniętą we wrapper -> użytkownik nie dotyka teraz oryginalnej funkcji tylko wrappera
wrapper przyjmuje dokładnie takie same argumenty co opakowana funkcja, aby mógł je przekazać opakowanej funkcji.

trudność polega na tym że ciężko przewidzieć jaką funkcję ktoś opakuje w dekorator i jakie ona będzie mieć argumenty





'''