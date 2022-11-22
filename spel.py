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
        self.level = 1
    
    def __str__(self):
        return f"Det här är {self.namn} han är en Ninja och har {self.hp} hp och {self.styrka} styrka. {self.namn} är i level {self.level}"

#---------------------------------

# Monsterklasser -----------------

class Monster_Armin():
    def __init__(self):
        self.namn = "Dunder Armin"
        self.hp = 75
        self.styrka = 50

class Monster_Romanian_Final_Boss():
    def __init__(self):
        self.namn = "Romanian Final Boss "
        self.hp = 1250
        self.styrka = 175

    def __str__(self):
        return f"Acest șef are {self.styrka} de putere și {1250} HP, el este regele!"

        #bild på romanian final boss

#---------------------------------

# Fällor -------------------------


#---------------------------------

# Dörr Funktioner ----------------

def monster_dörr(spelare):
    while True:
        print("AjAj ett storst monster dök upp?! Akta")
        monster_dörr_val = input("Vill du springa och är en pussy, TRYCK 1, annars om du är en riktig TOP G och vill fightas, TRYCK 2!")

        if monster_dörr_val == "1":
            print("din rotta, men spring för livet då?!")
            överlevnads_chans = random.randint(0,100)
            if överlevnads_chans > 50:
                print("Du överlevde och klarade springa ifrån monstret.")
                continue
            else:
                print("du dog din sopa")
                print("Spelet avslutas")
                break
        elif monster_dörr_val == "2":
            print("TOP G stannar och fightar och inte flightar, hoppas du vinner dock!")
            strid(spelare,monster)
        return spelare

def fälla_dörr(spelare):
    while True:
        print("Du har stött på en fälla. Akta dig!")
        fälla = random.choice("Bear trap")
        if fälla == "Bear trap":
            print("Ajj, du gick in i en bear trap, Du tappade 20 hp")
            spelare -= spelare.hp - 20

        return spelare
            

#---------------------------------

# Strid/fight Funktioner ---------

def strid(kar, mon):
    print("Slåss nu")

#.-------------------------------

def main():
        
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
        print("=================")
    else:
        print("Nu avslutas spelet!!!")

    meny_val_2 = input("Vad vill göras? Vill du gå vidare till din första utmaning, KLICKA DÅ 1. Om du vill kolla dina stats, KLICKA DÅ 2, och om du vill avsluta spelet, KLICKA 0")
    if meny_val_2 == "1":
        print("Du har stött på 3 plötsliga dörrar. Välj att antagligen att gå VÄNSTER, HÖGER eller FRAMMÅT?!" )
        vilken_dörr_1 = input("Vart vill du gå? -->")
        vilken_dörr_1 = vilken_dörr_1.lower()

        if vilken_dörr_1 == "vänster" or "höger" or "frammåt":
            print(f"Du har gått {vilken_dörr_1}")
            #lägg till kista och fälla
            bakom_dörren = random.choice("Monster", "Kista", "Fälla")
            if bakom_dörren == "Monster":
                #Lägg till monster
                spelare = monster_dörr(spelare)
            elif bakom_dörren == "Fälla":
                spelare = fälla_dörr(spelare)
    elif meny_val_2 == "2":
        print(spelare)



        print("next")



main()

    
   
    


# print(f"spelaren {spelare.namn} har {spelare.hp} hp kvar")



# def fight(kar, mon):
#     while spelare.hp > 0 or monster.hp >