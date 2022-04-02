

def outer_function(text):
    print("outer function")
    def inner_function(txt):
        print("inner function")
        return txt.upper()
    return inner_function(text)


outer_function("Ala ma kota")


"""
outer function
inner function

inner_function -> wewnętrzna funkcja
"""