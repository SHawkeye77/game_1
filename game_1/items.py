class Item:
    """ Base class for all items """
    def __init__(self, name, description, value):
        self.name = name  # Name of item
        self.description = description  # Description of item
        self.value = value  # Monetary value of item (in units)

    def __str__(self):
        # Prints a useful summary of item when print(<item>) is called
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Antimatter(Item):
    """ Child class for a vile of antimatter """
    def __init__(self, amount):
        self.amount = amount  # Amount, in grams, of antimatter in the vile
        super().__init__(name="Antimatter",
                         description="A small vile containing {} grams of antimatter.".format(self.amount),
                         value=self.amount)


class Weapon(Item):
    """ Child class of item to inherit weapons from """
    def __init__(self, name, description, value, damage):
        self.damage = damage  # Damage (in 'units') of the weapon
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class MetalBeam(Weapon):
    def __init__(self):
        super().__init__(name="Metal Beam",
                         description="A metal beam, about two feet long.",
                         value=0,
                         damage=5)


class Knife(Weapon):
    def __init__(self):
        super().__init__(name="Knife",
                         description="A simple knife, with a blade about six inches long.",
                         value=0,
                         damage=5)















