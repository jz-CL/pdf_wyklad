"""

@debug
def func(a, b, c):
    return a + b * c


print(func(3, b=2, c=4))


https://analityk.edu.pl/python-dekoratory/
https://bulldogjob.pl/news/1677-dekoratory-w-pythonie-czemu-warto-z-nich-korzystac

"""
def debug(func):
    def wrapper(*args, **kwargs):
        return f"DEKORATOR -> {func(*args, **kwargs)} <- DEKORATOR"
    return wrapper

@debug
def func(a, b, c):
    return a + b * c



print(func(3, b=2, c=4))


