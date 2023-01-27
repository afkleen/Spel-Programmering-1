import random
from time import sleep

# Olika Karaktärsklasser ----------
class Krigare():
    def __init__(self, namn):
        self.namn = namn
        self.styrka = 100
        self.hp = 550
        self.level = 1
        self.inventory = ["INVENTORY:","HPotion","HPotion"]
        self.speed = 25

    def __str__(self):
        return f"""
              Klass: Krigare

              Level:{self.level}

              HP:{self.hp}

              Strenght:{self.styrka}

              Speed:{self.speed}
              
              """



def ta_potion(Spelare):

    ta_potion = input("""
        Vill du ta en potion?
        | 1 | JA, EN HEALTH POTION
        | 2 | NEJ
        
        -->""")

    if ta_potion == "1":
        if "HPotion" in Spelare.inventory:
            Spelare.inventory == Spelare.inventory.remove("HPotion")
            Spelare.hp += 100
            print("SLUUUUUUUUUUUUUURP....")
            print("Du drack en HEALTH potion")
        else:
            print("Du har inga potions")
    elif ta_potion == "2":
        pass
    else: 
        print("du hann inte!")
    
    return Spelare
            


class Trollkarl():
    def __init__(self, namn):
        self.namn = namn
        self.styrka = 175
        self.hp = 375
        self.level = 2
        self.inventory = ["INVENTORY:","HPotion","HPotion"]
        self.speed = 60

    def __str__(self):
        return f"""
              Klass: Trollkarl

              Level:{self.level}

              HP:{self.hp}

              Strenght:{self.styrka}

              Speed:{self.speed}
              
              
              """

# ---------------------------------

# Monsterklasser -----------------


class Monster_Armin():
    def __init__(self):
        self.namn = "Dunder Armin"
        self.hp = 600
        self.styrka = 75
    def __str__(self):
        return f"Dunder Armin"
        


class Monster_Romanian_Final_Boss():
    def __init__(self):
        self.namn = "Romanian Final Boss "
        self.hp = 1250
        self.styrka = 175

    def __str__(self):
        return f"Acest șef are {self.styrka} de putere și {1250} HP, el este regele!"

        # bild på romanian final boss

# ---------------------------------


# MENY VAL -----------------------

def dörr(Spelare):

    print("""
    I SLUTET AV GROTTAN STÖTER DU PÅ TRE DÖRRAR
    """)

    ångrasig = input("""
        | 1 | Fortsätt in
        | 2 | Vänd om
    """)
    if ångrasig == 2:
        return Spelare
    else: 
        pass

    Monster = Monster_Armin()
    dörrinput = input("""
    _______________________
    Vilken dörr väljer du?  |
    | 1 | HÖGER             |
    | 2 | VÄNSTER           |
    | 3 | FRAMMÅT           |
    TTTTTTTTTTTTTTTTTTTTTTTT

    """)

    dörrar = [1,2,3]
    dörrval = random.choice(dörrar)
    if dörrval == 1:
        Spelare = strid(Spelare, Monster)
        
    elif dörrval == 2:
        kista(Spelare)
        
    elif dörrval == 3:
        fälla(Spelare)


# _______________________________
# Fällor -------------------------


# ---------------------------------

# Dörr Funktioner ----------------

#

# ---------------------------------


def intro():
    namn = input("Din gubbes namn: ")





    while True:
        KaraktärVal = input(
        "Ska din karaktär vara en | Krigare | eller | Trollkarl | ")
        KaraktärVal = KaraktärVal.lower()
        if KaraktärVal == "krigare":
            Spelare = Krigare(namn)
            break
        elif KaraktärVal == "trollkarl":
            Spelare = Trollkarl(namn)
            break
        else:
            print("du skrev fel")



    print(Spelare)
    return Spelare


# Strid/fight Funktioner ---------

def strid(Spelare, Monster):
    strid_val = (input("""

    DET ÄR DEN STORE DUNDER ARMIN
    
     _.--'''''--._
   .'             '.
  /                 \
 ;                   ;
 |                   |
 |                   |
 ;                   ;
  \ (`'--,    ,--'`) /
   \ \  _ )  ( _  / /
    ) )(')/  \(')( (
   (_ `""` /\ `""` _)
    \`"-, /  \ ,-"`/
     `\ / `""` \ /`
      |/\/\/\/\/\|
      |\        /|
      ; |/\/\/\| ;
       \`-`--`-`/
        \      /
         ',__,'
          q__p
          q__p
          q__p
          q__p

          | 1 | Tryck för att slåss -
    

    """))
    if strid_val == "1":
        while Monster.hp > 0 and Spelare.hp > 0:
            val = (input("""

            | 1 | SLÅ
            | 2 | SPRING"""))
            if val == "1":
                while True:
                    if Spelare.hp < 0:
                        exit()
                    elif Monster.hp < 0:
                        print("grattis du vann striden")

                        return Spelare
                        
                    attack = input(
                        """
                        ________________
                       | VÄLJ EN ATTACK |
                       TTTTTTTTTTTTTTTTTT
                    ______________________________________   
                    |                   |                 |
                    | (1) Light attack  | (2)Heavy attack |
                    |                   |                 |
                    |___________________|_________________|
                    
                    """

                    )
                    break
            elif val == "2":
                fly_chans = random.randint(1,2)
                if fly_chans == 1:
                    print("MONSTRET HAN IKAPP, DU DOG")
                    exit()
                elif fly_chans == 2:
                    print("DU SPRANG IFRÅN MONSTRET OCH KLARADE DIG.")
                    break

            if attack == "1":
                Monster.hp -= Spelare.styrka
                print(f"du träffade monsret och monstret har {Monster.hp} hp kvar")
                Spelare.hp -= Monster.styrka
                print(f"Monstret träffade dig och du har {Spelare.hp} hp kvar")
            elif attack == "2":
                crit_chans_spelare = round(random.uniform(0.7,2),1)
                crit_chans_monster = round(random.uniform(0.8,1.7),1)
                Monster.hp -= Spelare.styrka * crit_chans_spelare
                print(f"| Du träffade monstret och han har {Monster.hp} kvar. Du hade en damage multiplyer på {crit_chans_spelare}|")
                Spelare.hp -= Monster.styrka * crit_chans_monster
                print(f"| {Monster} prickade dig och du har {Spelare.hp} kvar. Monstret hade en damage multiplyer på {crit_chans_monster}")

            if Spelare.speed > 30 and not attack == "2" or attack=="1":

                hitrate = random.randint(1,2)

                if hitrate == 1:
                    Spelare.hp -= Monster.styrka
                    print(f"du blev träffad och har {Spelare.hp} hp kvar")
                elif hitrate == 2:
                    print("du duckade och monstret missade sin attack")

        if Spelare.hp >= 0:
            Spelare.level += 1
            print("""Grattis, du vann och gick upp en level""")
            print(f"Du är nu i level {Spelare.level}")
        elif Spelare.hp <= 0:
            print("Du dog")
            print("Spelet avslutas")
            exit()

    return Spelare




def fälla(Spelare):


    print("Du har stött på en fälla. Akta dig!")
    fälla = "Bear-trap"
    if fälla == "Bear-trap":
        print("Ajj, du gick in i en bear trap, Du tappade 20 hp")
        Spelare.hp = Spelare.hp - 20

    return Spelare


def kista(Spelare):
    items = ["HPotion","Yxa"]
    print("Du stöter på en kista.")
    val_1 = input("TRYCK | 1 | för att öppna kistan")
    if val_1 == "1":
        randomitem = random.choice(items)
        if randomitem == "HPotion":
            print("du fick en HEALTH potion")
            potion_val = input("""
            Tryck | 1 | om du vill dricka
            
            Tryck | 2 | om du vill lägga den i inventoryt
            """)
            if potion_val == "1":
                print("SLUURPPP... ")
                Spelare.hp = Spelare.hp + 100
                print(f"{Spelare.hp} hp har du!")
            elif potion_val == "2":
                print('ZZZIIIIIIIIIIIIPp... "lägger ner i ryggsäcken"')
                Spelare.inventory.append("HPotion")
        
        # ---------------------------
        elif randomitem == "Yxa":
            print("du fick en Yxa")
            potion_val = input("""
            Tryck | 1 | om du vill ha den som main vapen
            """)
            if potion_val == "1":
                print("Tjiiiiiing ")
                Spelare.styrka = Spelare.styrka + 120
                print(f"""Du fick precis 120 mer styrka.
                """)
                print(f"du har nu {Spelare.styrka} styrka!")
            else: 
                print("Ok. KASTAR BORT YXAN......")

    return Spelare
        # ---------------------------


def stats(Spelare):
    print(Spelare)


def meny(Spelare):

    while True:
        print("""
    MENY

    Tryck | 1 | för att kolla dina stats!
    Tryck | 2 | för att öppna din ryggsäck!
    Tryck | 3 | för att gå vidare
    Tryck | 0 | för att avsluta spelet.

    Ditt val --> 
    """)
        meny_val = input()

        if meny_val == "1":
            print("""
            STATS
            """)
            stats(Spelare)
        elif meny_val == "2":
            print(Spelare.inventory)
            ta_potion(Spelare)
        elif meny_val == "3":
            print("""

            Fortsätter djupare in i grottan......
            
            """)
            break
        elif meny_val == "0":
            print("Spelet avslutas")
            exit()
        else:
            print("välj rätt din sopa")


# .-------------------------------


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

    meny(Spelare)

    Monster = Monster_Armin()

    while Spelare.level < 3 or Spelare.hp > 0:
        dörr(Spelare)
        meny(Spelare)
        if Spelare.level > 2:
            print("""
.--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--.
/ .. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \
\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/ /
 \/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /
 / /\/ /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /\/ /\
/ /\ \/`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\ \/\ \
\ \/\ \                                                    /\ \/ /
 \/ /\ \                                                  / /\/ /
 / /\/ /                                                  \ \/ /\
/ /\ \/               GRATTIS DU VANN SPELET               \ \/\ \
\ \/\ \                                                    /\ \/ /
 \/ /\ \                                                  / /\/ /
 / /\/ /                                                  \ \/ /\
/ /\ \/                                                    \ \/\ \
\ \/\ \.--..--..--..--..--..--..--..--..--..--..--..--..--./\ \/ /
 \/ /\/ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ /\/ /
 / /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\
/ /\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \
\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `' /
 `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'
        
       
        
        """)
            exit()
        elif Spelare.hp <= 0: 
            print("DU DOG OCH FÖRLORADE SPELET")
            exit()

main()

