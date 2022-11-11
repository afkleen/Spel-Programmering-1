import random 

# Olika Karaktärsklasser ----------
class Krigare():
    def __init__(self, namn):
        self.namn = namn
        self.styrka = 100
        self.hp = 550
        self.level = 1
    def __str__(self):
        return f"Det här är {self.namn} han är en Krigare och har {self.hp} hp och {self.styrka} styrka. {self.namn} är i level {self.level}"
    

class Trollkarl():
    def __init__(self, namn):
        self.namn = namn
        self.styrka = 175
        self.hp = 350
        self.level = 1
    
    def __str__(self):
        return f"Det här är {self.namn} han är en Trollkarl och har {self.hp} hp och {self.styrka} styrka. {self.namn} är i level {self.level}"

class Ninja():
    def __init__(self, namn):
        self.namn = namn
        self.styrka = 90
        self.hp = 350
    
    def __str__(self):
        return f"Det här är {self.namn} han är en Ninja och har {self.hp} hp och {self.styrka} styrka. {self.namn} är i level {self.level}"

#---------------------------------

# Monsterklasser -----------------

class Monster_Armin():
    def __init__(self):
        self.hp = 444

#---------------------------------

# Dörr Funktioner ----------------

def monster_dörr():
    print("AjAj ett storst monster dök upp?! Akta")
    monster_dörr_val = input("Vill du springa tryck  ")





namn = input("Vad ska din gubbe heta? -->")

KaraktärVal = input("Ska din karaktär vara en [Krigare], [Trollkarl] eller [Ninja]")

KaraktärVal = KaraktärVal.lower()

if KaraktärVal == "krigare":
    spelare = Krigare(namn)
elif KaraktärVal == "trollkarl":
    spelare = Trollkarl(namn)
elif KaraktärVal == "ninja":
    spelare = Ninja(namn)
else:
    print("Du skrev fel")

print(spelare)


meny_val_1 = input("Klicka 1 om du vill gå vidare eller klicka 2 om du vill avsluta spelet. -->")
if meny_val_1 == "1":
    print(f"{spelare.namn} går vidare")
else:
    print("gå hem")
   
    


# print(f"spelaren {spelare.namn} har {spelare.hp} hp kvar")



# def fight(kar, mon):
#     while spelare.hp > 0 or monster.hp >