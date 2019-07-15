"""
Items classes should always follow the format:
Capital letters for the start of new words.
"""


class Item:
    """ Base class for all items """
    def __init__(self, name, description):
        self.name = name  # Name of item
        self.description = description  # Description of item

    def use(self, item):  # MAYBE NOT HAVE 'item' PARAM HERE?
        """
        Call when you want to use the current (self) item on the item that is passed in.
        e.g. use key on door
        """
        # Override in child class if you want to have the object able to be used on something
        print("You can't do that.")

    def interact(self):
        """
        Call when you want to interact with the current (self) item
        e.g. interact with door
        """
        # Override in child class if you want to have the object interact-able
        print("Nothing happens.")


class Antimatter(Item):
    """ Child class for a vile of antimatter """
    def __init__(self, amount):
        self.amount = amount  # Amount, in grams, of antimatter in the vile
        super().__init__(name="Antimatter",
                         description="A small vile containing {} grams of antimatter.".format(amount))

    def interact(self):
        print("By interacting with the antimatter, you increased its power!")
        self.amount += 1
        # IS THERE A MORE EFFICIENT WAY TO CHANGE THE DESCRIPTION? DOESN'T CHANGE NATURALLY...
        super().__init__(name="Antimatter",
                         description="A small vile containing {} grams of antimatter.".format(self.amount))
        return


class Weapon(Item):
    """ Child class of item to inherit weapons from """
    def __init__(self, name, description, damage):
        self.damage = damage  # Damage (in 'units') of the weapon
        super().__init__(name, description)


class MetalBeam(Weapon):
    def __init__(self):
        super().__init__(name="Metal Beam",
                         description="A metal beam, about two feet long.",
                         damage=5)


class Knife(Weapon):
    def __init__(self):
        super().__init__(name="Knife",
                         description="A simple knife, with a blade about six inches long.",
                         damage=5)















