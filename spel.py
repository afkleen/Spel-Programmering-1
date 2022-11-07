import random

namn = input("Vad ska din gubbe heta? -->")

# Olika Karaktärsklasser ----------
class Krigare():
    def __init__(self, namn):
        self.namn = namn
        self.dmg = random.randint(0.54,1) * 100
        self.hp = 100

class Trollkarl():
    def __init__(self):
        self.dmg = random.randint(0.33,0.5) * 100
        self.hp = 100

class Ninja():
    def __init__(self):
        def __init__(self):
            self.dmg = 100

#---------------------------------

# DIN KARAKTÄR ----------
class Karaktär():
    def __init__(self):
        self.level = 1
        self.name = input("Vad heter din karaktär")
        self.klass = input("Ska din karaktär vara en [Krigare], [Trollkarl] eller [Ninja]")

#------------------------

def main():
    spelare = Karaktär()
    if  == "Krigare":
        Spelare = Krigare()

