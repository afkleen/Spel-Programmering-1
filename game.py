import random 
from time import sleep

# print("hej")
# sleep(2)
# print("hallå ")



# Olika Karaktärsklasser ----------
class Krigare():
    def __init__(self, namn):
        self.namn = namn
        self.styrka = 100
        self.hp = 550
        self.level = 1
        self.inventory = ["HPotion", "SPotion"]

    def __str__(self):
        return f"""
              Klass: Krigare

              Level:{self.level}

              HP:{self.hp}

              Strenght:{self.styrka}"""

    # def ta_potion():
    #     self.potions -=1
    #     self.hp += 10    

class Trollkarl():
    def __init__(self, namn):
        self.namn = namn
        self.styrka = 175
        self.hp = 350
        self.level = 1
        self.inventory = ["HPotion", "SPotion"]
    
    def __str__(self):
        return f"Det här är {self.namn} han är en Trollkarl och har {self.hp} hp och {self.styrka} styrka. {self.namn} är i level {self.level}"

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








# MENY VAL -----------------------

def dörr(Spelare):

    print("DU GÅR IN I GROTTAN OCH STÖTER PÅ TRE DÖRRAR!!!")
    
    dörrval = input("vill du gå 1. vänster 2. höger 3. frammåt -->")
    dörrval = dörrval.lower

    if dörrval == [1,2,3]:
        random.choice[1,2,3]
    if True:
        match dörrval:

            case "1":
                print("du kommer nu kriga")
                Spelare = strid(Spelare, Monster)

            case "2":
                print("du gick på en fälla")
                Spelare = fälla()

            case "3":
                print("du stötte på en kista")
                Spelare = kista()


    
# _______________________________
# Fällor -------------------------


#---------------------------------

# Dörr Funktioner ----------------

# 

#---------------------------------



def intro():
    namn = input("Din gubbes namn: ")

    KaraktärVal = input("Ska din karaktär vara en [Krigare], [Trollkarl] eller [Ninja]")

    KaraktärVal = KaraktärVal.lower()

    if KaraktärVal == "krigare":
        Spelare = Krigare(namn)
    elif KaraktärVal == "trollkarl":
        Spelare = Trollkarl(namn)
    else:
        print("Du skrev fel")

    print(Spelare)
    return Spelare


# Strid/fight Funktioner ---------

def strid(Spelare, monster):
    print("Slåss nu")
    Spelare.hp -= 5

def fälla(Spelare):
    
    while True:
        print("Du har stött på en fälla. Akta dig!")
        fälla = "Bear-trap"
        if fälla == "Bear-trap":
            print("Ajj, du gick in i en bear trap, Du tappade 20 hp")
            Spelare = Spelare.hp - 20

        return Spelare

def kista(Spelare):

    items = ["HPotion", "SPotion", "Svärd"]
    print("Du stöter på en kista.")
    val_1 = input("TRYCK | 1 | för att öppna kistan")
    if val_1 == "1":
        randomitem = random.choice(items)
        if randomitem == "HPotion" or "SPotion" or "Svärd":
            print("du fick en HEALTH potion")
            potion_val = input("""
            Tryck | 1 | om du vill dricka
            
            Tryck | 2 | om du vill lägga den i inventoryt
            """)
            if potion_val == "1":
                print("SLUURPPP... ")
                Spelare = Spelare.hp + 100
            elif potion_val == "2":
                print('ZZZIIIIIIIIIIIIPp... "lägger ner i ryggsäcken"')
                Spelare.inventory.append("HPotion")
            return Spelare
        #---------------------------
        elif randomitem == "SPotion":
            print("du fick en STRENGTH potion")
            potion_val = input("""
            Tryck | 1 | om du vill dricka
            
            Tryck | 2 | om du vill lägga den i inventoryt
            """)
            if potion_val == "1":
                print("SLUURPPP... ")
                Spelare = Spelare.styrka + 100
            elif potion_val == "2":
                print('ZZZIIIIIIIIIIIIPp... "lägger ner i ryggsäcken"')
                Spelare.inventory.append("SPotion")
            return Spelare
        #---------------------------
        elif randomitem == "Svärd":
            print("Svärd")


def stats(Spelare):
    print(Spelare)

def meny(Spelare):
    meny_val = input("""
    MENY

    Tryck | 1 | för att kolla dina stats!
    Tryck | 2 | för att öppna din ryggsäck!
    Tryck | 3 | för att gå vidare
    Tryck | 0 | för att avsluta spelet.
    """)

    if meny_val == "1":
        print("KOLLAR STATS")
        stats(Spelare)
    elif meny_val == "2":

#.-------------------------------


def main():
    
    print("""
    
    Du går själv i skogen och är ute på äventyr. 
    Det är tjock dimma ute och det är svårt att se men du 
    tittar ner i marken och få då syn på ett brev. Brevet följer....""")

    sleep(3)

    print("""   
  ______________________________
 / \                             \.
|   | Hej din äventyrare, vad kul|.
 \_ | att du är här. Grottan fra-|.
    | mför dig är en magisk      |.
    | portal. Gå in i grottan för|.
    | att påbörja äventyret eller|.
    | vänd om för att fly från de|.
    | oupptäckta                 |.
    |                            |.
    |                            |.
    | Tryck 1. Gå fram           |.
    |       2. Vänd om           |.
    |                            |.
    |                            |.
    |   _________________________|___
    |  /                            /.
    \_/dc__________________________/.
""")

    sleep(2)
    
    startval = input("VAD VÄLJER DU?: -->")
    i = 0
    while startval not in ["1", "2"]:
        startval = input("VAD VÄLJER DU?: -->")
    
    if startval == "1":
        Spelare = intro()
        
    else:
        print("spelet avslutas!")
        sleep(1.5)
        print("hejdå")
        exit()

        
    
    # while Spelare.level < 10 or Spelare.hp <= 0:
    #     Spelare = dörr(Spelare)
       
main()

# print("""
# Längre in går du i grottan och stöter på tre dörrar,
# Tryck | 1 | för att öppna vänstra dörren
# Tryck | 2 | för dörren rakt fram &
# Tryck | 3 | för att öppna höger
# För att springa ut tryck | 0 |
# """)

# dörr_val = input("Vart vill du gå? -->")

# if dörr_val == "0":
#     print("Jag han ut; WHEWWWWW!")
#     print("SPELET AVSLUTAS")
#     exit()
# else:
#     random_dörr = random.choice(["fälla", "kista"])

#     if random_dörr == "fälla":
#         fälla(Spelare)
#     elif random_dörr == "kista":
#         kista(Spelare)


# namn = input("Vad ska din gubbe heta? -->")

# KaraktärVal = input("Ska din karaktär vara en [Krigare], [Trollkarl] eller [Ninja]")

# KaraktärVal = KaraktärVal.lower()

# if KaraktärVal == "krigare":
#     spelare = Krigare(namn)
# elif KaraktärVal == "trollkarl":
#     spelare = Trollkarl(namn)
# elif KaraktärVal == "ninja":
#     spelare = Ninja(namn)
# else:
#     print("Du skrev fel")

# print(spelare)


# meny_val_1 = input("Klicka 1 om du vill gå vidare eller klicka 2 om du vill avsluta spelet. -->")
# if meny_val_1 == "1":
#     print(f"{spelare.namn} går vidare")
# else:
#     print("gå hem")

# meny_val_2 = input("Vad vill göras? Vill du gå vidare till din första utmaning, KLICKA DÅ 1. Om du vill kolla dina stats, KLICKA DÅ 2, och om du vill avsluta spelet, KLICKA 0")
# if meny_val_2 == "1":
#     print("Du har stött på 3 plötsliga dörrar. Välj att antagligen att gå VÄNSTER, HÖGER eller FRAMMÅT?!" )
#     vilken_dörr_1 = input("Vart vill du gå? -->")
#     vilken_dörr_1 = vilken_dörr_1.lower()

#     if vilken_dörr_1 == "vänster" or "höger" or "frammåt":
#         print(f"Du har gått {vilken_dörr_1}")
#         #lägg till kista och fälla
#         bakom_dörren = "Monster"
#         if bakom_dörren == "Monster":
#             #Lägg till monster
#             monster_dörr()

#     print("next")




    
   
    


# print(f"spelaren {spelare.namn} har {spelare.hp} hp kvar")



# def fight(kar, mon):
#     while spelare.hp > 0 or monster.hp

# def monster_dörr():
#     while True:
#         print("AjAj ett storst monster dök upp?! Akta")
#         monster_dörr_val = input("Vill du springa och är en pussy, TRYCK 1, annars om du är en riktig TOP G och vill fightas, TRYCK 2!")

#         if monster_dörr_val == "1":
#             print("din rotta, men spring för livet då?!")
#             överlevnads_chans = random.randint(0,100)
#             if överlevnads_chans > 50:
#                 print("Du överlevde och klarade springa ifrån monstret.")
#                 continue
#             else:
#                 print("du dog din sopa")
#                 break
#         elif monster_dörr_val == "2":
#             print("TOP G stannar och fightar och inte flightar, hoppas du vinner dock!")
#             strid(spelare, random.choice(Monster_Armin))