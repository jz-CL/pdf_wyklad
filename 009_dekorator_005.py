"""
dlatego dekorator powinien mieć taką postać:
def wrapper(*args, **kwargs)

dzięki temu można opakować dowolną funkcję

"""


def my_decorator(func):
    def wrapper(*args, **kwargs):
        return f"DECORATED -> {func(*args, **kwargs)} <- DECORATED"
    return wrapper



def hello_name(name):
    return f"Hello, {name}!"

def hello_two_names(first_name, second_name):
    return f"Hello, {first_name} and {second_name}!"


print(hello_name("Krzysiek"))
# Hello, Krzysiek!

print(my_decorator(hello_name)("Krzysiek"))
# DECORATED -> Hello, Krzysiek! <- DECORATED

print(hello_two_names("Krzysiek", "Olga"))
# Hello, Krzysiek and Olga!

print(my_decorator(hello_two_names)("Krzysiek", "Olga"))
# DECORATED -> Hello, Krzysiek and Olga! <- DECORATED


"""
tu dekorator używany jest w formie
dekorator(dekorowana_funkcja)(argumenty)

str. 130
"""