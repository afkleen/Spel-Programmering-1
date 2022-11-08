import random

namn = input("Vad ska din gubbe heta? -->")

KaraktärVal = input("Ska din karaktär vara en [Krigare], [Trollkarl] eller [Ninja]")


# Olika Karaktärsklasser ----------
class Krigare():
    def __init__(self, namn):
        self.namn = namn
        self.dmg = random.randint(0,1) * 100
        self.hp = 100

class Trollkarl():
    def __init__(self, namn):
        self.dmg = random.randint(0,1) * 100
        self.hp = 100

class Ninja():
    def __init__(self, namn):
        def __init__(self):
            self.dmg = 100

#---------------------------------

if KaraktärVal == "Krigare":
    spelare = Krigare(namn)
    print("Du är en krigare")
elif KaraktärVal == "Trollkarl":
    spelare = Trollkarl(namn)
    print("Du är en Trollkarl")
elif KaraktärVal == "Ninja":
    spelare = Ninja(namn)
    print("Du är en Ninja")
