def greet(name):
    if name == "Johnny":
        print(f"Hello {name}!, where are you?")
    else:
        print(f"Hello {name}! hope you are doing well")
    
greet("James")
greet("Jane")
greet("Johnny")
greet("Jim")

def are_you_playing_banjo(name):
    if name.capitalize().startswith("R"):
        print(f"{name}, plays banjo!")
    else:
        print(f"{name} does not play banjo")
    
are_you_playing_banjo("ruby")
are_you_playing_banjo("Raj")
are_you_playing_banjo("Kittu")