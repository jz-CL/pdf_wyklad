

def say_hello(name):
    print(f"Hey {name}!")

def say_goodbye(name):
    print(f"Bye {name}!")


def greet_kryśka(greeting):
    return greeting("Kryśka")

greet_kryśka(say_hello)

greet_kryśka(say_goodbye)


"""
Hey Kryśka!
Bye Kryśka!
"""