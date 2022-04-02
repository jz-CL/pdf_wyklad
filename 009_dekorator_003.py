def greeting(time):
    def morning_greteng(name):
        print(f"Good morning, {name}!")

    def afternoon_greeting(name):
        print(f"Good afternoon, {name}!")

    def late_night_greeting(name):
        print(f"Good night, {name}!")

    if time == "morning":
        return morning_greteng

    if time == "afternoon":
        return late_night_greeting


greeting_fun = greeting("morning")
greeting_fun("John")


"""
Good morning, John!

greeting -> funkcja - fabryka
"""