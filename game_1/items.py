"""
Items classes should always follow the format:
Capital letters for the start of new words.
Examples: Book, GarageDoor, ElectricalCable, etc.
"""
import scenarios
import world


class Item:
    """ Base class for all items """
    def __init__(self, name, description, can_pick_up=True):
        self.name = name  # Name of item
        self.description = description  # Description of item
        self.can_pick_up = can_pick_up  # Can the user add this to their inventory

    def use(self, **kwargs):
        """
        Call when you want to use the current (self) item on the item that is passed in (in overridden methods of use).
        e.g. use key on door
        NOTE: Must always be able to accept a variable number of arguments!
        """
        # Override in child class if you want to have the object able to be used on something
        print("You can't do that.")

    def interact(self, **kwargs):
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


class Couch(Item):
    def __init__(self):
        super().__init__(name="Couch", can_pick_up=False,
                         description="A sleek, black leather couch.")

    def interact(self):
        print("Huh, pretty comfy.")


class Tablet(Item):
    def __init__(self):
        super().__init__(name="Tablet", can_pick_up=False,
                         description="A touch-screen pad, held at shoulder-height by a narrow, cylindrical stand.")

    def interact(self): ### TO BE CHANGED (of course)
        print("You play angry birds.")


class Rover(Item):
    def __init__(self, locked=True, player_inside=False):
        self.locked = locked
        self.player_inside = player_inside  # True if the player is inside and piloting the rover
        super().__init__(name="Rover", can_pick_up=False,
                         description="A modest rover. The cabin is tube-shaped, and there's four huge wheels"
                                     " jutting out from each side.")

    def interact(self): #TO BE EXPANDED ON (OBVIOUSLY)
        if self.locked:
            print("It's locked. Looks like it requires a key-code to enter.")
        else:
            print("It's unlocked! You climb inside.")
            self.player_inside = True  # MAKE SURE WHEN YOU LEAVE ROVER THIS SWITCHES BACK TO FALSE!


class GarageLever(Item):
    # This lever controls opening/closing the garage bay door
    def __init__(self, garage_down=True):
        self.garage_down = garage_down
        super().__init__(name="Lever", can_pick_up=False,
                         description="A bulky mechanical lever. There's a wire attached to it that follows the "
                                     "dome above and ends at the garage door.")

    def interact(self, **kwargs):
        # Getting the player object
        for key, value in kwargs.items():
            if key == "player":
                player = value
        scenarios.opened_garage(player, self)


class Bench(Item):
    def __init__(self):
        super().__init__(name="Bench", can_pick_up=False,
                         description="A sleek, black leather couch.")

    def interact(self):
        print("It's not too comfy. Better than standing, though.")


class Plant(Item):
    def __init__(self):
        super().__init__(name="Plant",
                         description="Looks like a Ficus Danielle, similar-looking to one at your apartment on Terra. "
                                     "It's clearly fake.")


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

    # NOTE: In order for this to work, we assume all items will be objects...
    def use(self, **kwargs):
        destroyed_antimatter = False
        for label, arg in kwargs.items():
            if label == "item":
                if arg.name.title() == "Antimatter":
                    print("With a swipe of the knife you cut open the antimatter. "
                          "A millisecond later you notice your mistake, just in time for"
                          " the world to collapse around you.")
                    destroyed_antimatter = True
            # Should always pass in a player object
            if label == "player":
                player = arg  # Will gather the player object
        if destroyed_antimatter:
            player.hp = 0


class Food(Item):
    def __init__(self, name, description, eat_response="Tastes like chicken"):
        self.eat_response = eat_response
        super().__init__(name=name, description=description, can_pick_up=True)

    def eat(self):
        print(self.eat_response)


class Drink(Item):
    def __init__(self, name, description, drink_response="*gulp*"):
        self.drink_response = drink_response
        super().__init__(name=name, description=description, can_pick_up=True)

    def drink(self):
        print(self.drink_response)
