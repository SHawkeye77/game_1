"""
Holds items specifically made in the research dome
"""

from items import Item
from items_all.items_general import *

############################# Achebe Office Items ############################
class WetWipes(Item):
    def __init__(self):
        super().__init__(name=["Wet Wipes", "Wipes"], can_pick_up=True,
            description="A pack of antibacterial wet wipes")

class Drawers(Item):
    def __init__(self, description="A set of desk drawers."):
        super().__init__(name=["Drawers","Drawer"],can_pick_up=False,
            description=description)

    def interact(self, player):
        print("You open up the drawers. Inside, there are some post-it "
            "notes, wet wipes, and a book with the title: \"The Sirens of "
            "Titan\".")

class AchebePhd(Item):
    def __init__(self):
        super().__init__(name=["PhD Certificate", "Certificate"],
            description="A framed, mechanical engineering PhD Certificate "
            "from University College London", can_pick_up=True)

class Altoids(Food):
    def __init__(self):
        super().__init__(name=["Tin of Altoids", "Altoids"],
            description="A small red tin labeled \"ALTOIDS - CURIOUSLY "
            "STRONG MINTS\"", eat_response="Curiously strong! Yum!")

class Poster(Item):
    def __init__(self):
        super().__init__(name=["Movie Poster", "Poster", "Star Wars Poster"],
            can_pick_up=True, description="It's in another language, but it "
            "depicts a man on a hill next to a woman and two robots. "
            "A dark head looms behind them. The signature "
            "says \"Carrie Fisher\".")

class Pen(Item):
    def __init__(self, description="A gold and black ballpoint pen. It "
        "says \"Montblanc\" on it."):
        super().__init__(name=["Pen"], can_pick_up=True, description=\
            description)

    def use(self, item, player):
        if "paper" in [name.lower() for name in item.name]:
            w = input("What do you want to write on the paper? ")
            print("You write \"" + w + "\" on the paper.")
        else:
            print("Nothing happens.")

class PostItNotes(Item):
    def __init__(self):
        super().__init__(name=["Post-It Notes", "Post It Notes", "Post It"],
            can_pick_up=True, description="A set of yellow Post-It notes")

############################# Gomez Office Items ############################
class WhiskeyGlass(Item):
    def __init__(self):
        super().__init__(name=["Whiskey Glass", "Glass"], can_pick_up=True,
            description="A small glass for booze")


############################## Zlo Office Items #############################
class ArmChair(Item):
    def __init__(self):
        super().__init__(name=["Armchair", "Arm Chair", "Comfy Chair", 
            "Lounge Chair"], can_pick_up=False, description="A red-checkered "
            "armchair. Looks pretty comfy!")

    def interact(self, player):
        print("Ah, just as comfy as it looked!")

class NobelPrize(Item):
    def __init__(self):
        super().__init__(name=["Award", "Framed Award", "Nobel Prize"],
            can_pick_up=True, description="It's a golden coin about the size "
            "of two quarters. It's engraved with the portrait of a man "
            "and the phrases \"Nat. MDCCCXXXIII Ob. MDCCCXCVI\" and "
            "\"ALFR. NOBEL\"")

    def interact(self, player):
        print("Flipping it over you can see the inscriptions on the back: "
            "\"Inventas vitam iuvat excoluisse per artes\", "
            "\"REG. ACAD. SCIENT. SUEC.\", \"Erik Lindberg\", and \"O. ZLO "
            "MMXXX\"")

class RussianNestingDoll(Item):
    def __init__(self):
        self.times_opened = 0
        self.layers = 5
        super().__init__(name=["Russian Nesting Doll", "Nesting Doll", "Doll"],
            can_pick_up=True, description="A nesting doll. A faded drawing "
            "of a babushka is on it.")

    def interact(self, player):
        self.times_opened += 1
        if (self.times_opened >= self.layers):
            print("TODO") # PRESENT PLAYER WITH SOMETHING THAT'S HIDING IN THE CENTER!!!!!!!!!!!!!!!!!!!!
        else:
            print("You remove a layer from the doll. Another babushka smiles "
                "back at you.")

class Map(Item):
    def __init__(self, description="A huge map nailed into the wall. "
        "Its description reads: \"Czechoslovakia 1970\"."):
        super().__init__(name=["Map", "Czechoslovakia Map"], 
            can_pick_up=False, description=description)

class NewtonsCradle(Item):
    def __init__(self):
        super().__init__(name=["Newtons Cradle", "Newton's Cradle", "Cradle"], can_pick_up=True,
            description="The five-ball classic physics toy")
    def interact(self, player):
        print("You pull back and let go one of the balls.\nTick - Tick - Tick - Tick..."
        "\nThe motion slowly fades out...")

class Scarf(Item):
    def __init__(self, description=""):
        super().__init__(name=["Scarf", "C.D. Oro Scarf"], can_pick_up=True, description=description)
    def interact(self, player):
        print("You wave it around your head like a football ultra.")

class EspressoMachine(Item):
    def __init__(self):
        super().__init__(name=["Espresso Machine", "Espresso"], can_pick_up=False,
            description="A black Nespresso espresso machine. Looks like it takes espresso pods, none of which "
            "seem to be anywhere nearby. Shame, you could use a shot...")
    def interact(self, player):
        print("You turn it on and within seconds hot water begins to flow out, tainting the already "
        "coffee-stained papers even more.")

class ScatteredPapers(Item):
    def __init__(self):
        super().__init__(name=["Scattered Papers", "Papers", "Notes", "Scattering of Papers"], can_pick_up=False,
            description="An unorganized jumble of research notes and legal paperwork. Most are coffee-stained.")
    def interact(self, player):
        print("Picking up a sheet you start reading:\n\"AN ANALYSIS OF EXTREME SURVIVAL CAPABILITY ASSETS IN "
        "TARDIGRADES\"\nConfusing... You pick up another:\n\"TERRAN ITEM RETRIEVEMENT REQUEST FORM\"\n"
        "It's not filled out.")