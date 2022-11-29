import random 

def intro():
        namn = input("Vad ska din gubbe heta? -->")
        KaraktärVal = input("Ska din karaktär vara en [Krigare], [Trollkarl] eller [Ninja]").lower()
        Player(namn,KaraktärVal)
        Player.spleare_Val()
        return Player

# Olika Karaktärsklasser ----------
class Player():
    def __init__(self, namn,karaktär):
        self.namn = namn
        self.level = 1
        self.styrka: int
        self.hp: int
        self.printout = ""
        self.karaktär = karaktär

    def __str__(self):
        return self.printout

    def spleare_Val(self):
    
        krigare = Krigare()
        trollkarl = Trollkarl()
        ninja = Ninja()
        kak_val = 1
        if kak_val == 1:
            match self.karaktär:

                case "krigare":
                    self.hp = krigare.hp 
                    self.styrka = krigare.styrka
                    self.printout = "Det här är {self.namn} han är en Krigare och har {self.hp} hp och {self.styrka} styrka. {self.namn} är i level {self.level}"
                  
            
                case "trollkarl":
                    self.hp = trollkarl.hp 
                    self.styrka = trollkarl.styrka
                    self.printout = f"Det här är {self.namn} han är en Trollkarl och har {self.hp} hp och {self.styrka} styrka. {self.namn} är i level {self.level}"

                case "ninja":
                    self.hp = ninja.hp 
                    self.styrka = ninja.styrka
                    self.printout =  f"Det här är {self.namn} han är en Ninja och har {self.hp} hp och {self.styrka} styrka. {self.namn} är i level {self.level}"
    

class Krigare():
    def __init__(self):
        self.styrka = 100
        self.hp = 55
    
class Trollkarl():
    def __init__(self):
        self.styrka = 175
        self.hp = 35

class Ninja():
    def __init__(self):
        self.styrka = 90
        self.hp = 350
#---------------------------------

class Item():
    def __init__(self):
        self.styrka: int
        

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
    spel_igång = True
    while spel_igång:
        print("AjAj ett storst monster dök upp?! Akta")
        monster_dörr_val = input("Vill du springa och är en pussy, TRYCK 1, annars om du är en riktig TOP G och vill fightas, TRYCK 2!")
        match monster_dörr_val:
            case "1": 
                print("Din rotta, men spring för livet då?!")
                överlevnads_chans = random.randrange()
                if överlevnads_chans > 0.5:
                    print("Du överlevde och klarade springa ifrån monstret.")   
                else:
                    print("""Du dog din sopa
                             Spelet avslutas""")
                    break
            case "2":

                print("TOP G stannar och fightar och inte flightar, hoppas du vinner dock!")
                # strid(spelare,monster)
        


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
        
    while True:   

        spelare = intro()     


        meny_val_1 = input("1. gå vidare | 2. stats")
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
                val = ["Monster","Kista", "Fälla"]
                bakom_dörren = random.choice(val)
                
                match bakom_dörren:
                    case "Monster":
                        spelare = monster_dörr(spelare)
                    case "Fälla":
                        spelare = fälla_dörr(spelare)

        elif meny_val_2 == "2":
            print(spelare)
            #Göra nästa



            print("next")



main()

    
   
    


# print(f"spelaren {spelare.namn} har {spelare.hp} hp kvar")



# def fight(kar, mon):
#     while spelare.hp > 0 or monster.hp >