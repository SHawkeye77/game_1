"""
Items classes should always follow the format:
Capital letters for the start of new words.
Examples: Book, GarageDoor, ElectricalCable, etc.

NOTE: Items are interacted with by their associated item.name attribute. It should be intuitive to the player.
NOTE: Items must be able to accept **kwargs for all "interact" and "use" overrides!
- When you add "use" function overrides, make sure to account for when they are called with objects that will do nothing,
  and print a default response e.g. "Nothing happens."
"""
import scenarios
import world


class Item:
    """ Base class for all items """
    def __init__(self, name, description, can_pick_up=True):
        self.name = name  # Name of item
        self.description = description  # Description of item
        self.can_pick_up = can_pick_up  # Can the user add this to their inventory

    def use(self, item, player):
        """
        Used for "use _____ on _____" input
        Call when you want to use the current (self) item on the item that is passed in (in overridden methods of use).
        e.g. use key on door

        Args:
            item (object): other item we are going to use the current (self) item on.
            player (object): current user's player object
        Returns:
            N/A but uses self object on item object
        """
        # Override in child class if you want to have the object able to be used on something
        print("Nothing happens.")

    def interact(self, **kwargs):
        """
        Used for "interact with _____" input
        Call when you want to interact with the current (self) item
        e.g. interact with door
        """
        # Override in child class if you want to have the object interact-able
        print("Nothing happens.")


class Lock(Item):
    def __init__(self):
        super().__init__(name="Lock", can_pick_up=False,
                         description="An old, bulky, mechanical lock.")


class Antimatter(Item):
    """ Child class for a vile of antimatter """
    def __init__(self, amount):
        self.amount = amount  # Amount, in grams, of antimatter in the vile
        super().__init__(name="Antimatter",
                         description="A small vile containing {} grams of antimatter.".format(amount))

    def interact(self, **kwargs):
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

    def interact(self, **kwargs):
        print("Huh, pretty comfy.")


class Tablet(Item):
    def __init__(self):
        super().__init__(name="Tablet", can_pick_up=False,
                         description="A touch-screen pad, held at shoulder-height by a narrow, cylindrical stand.")

    def interact(self, **kwargs): ### TO BE CHANGED (of course)
        print("You play angry birds.")


class Rover(Item):
    def __init__(self, locked=True, player_inside=False):
        self.locked = locked
        self.player_inside = player_inside  # True if the player is inside and piloting the rover
        super().__init__(name="Rover", can_pick_up=False,
                         description="A modest rover. The cabin is tube-shaped, and there's four huge wheels"
                                     " jutting out from each side.")

    def interact(self, **kwargs): #TO BE EXPANDED ON (OBVIOUSLY)
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


class Chair(Item):
    def __init__(self):
        super().__init__(name="Chair", can_pick_up=False,
                         description="A standard, wooden chair.")

    def interact(self, **kwargs):
        print("Surprisingly comfy.")


class Table(Item):
    def __init__(self, description="A large table with a polished finish."):
        super().__init__(name="Table", can_pick_up=False,
                         description=description)


class Clock(Item):
    def __init__(self, time_location="Minneapolis"):
        self.time_location = time_location
        super().__init__(name=time_location + " Clock", can_pick_up=True,
                         description="A traditional-looking clock set to " + self.time_location + " local time.")


class DeadCommunicationsDirector(Item):
    def __init__(self):
        super().__init__(name="Communications Director", can_pick_up=False,
                         description="It is clear something awful happened to the director.\n"
                                     "His skin is, for the most part, torn. While some tears look like cuts, others "
                                     "are large enough to expose patches of his anatomy underneath... "
                                     "The intact portions of the man's skin are not normal either; at these spots "
                                     "the skin has clumped together and begun to sag from the man's body.")

    def interact(self, **kwargs):
        print("Yeah right, no way I'm touching that.")


class Bench(Item):
    def __init__(self):
        super().__init__(name="Bench", can_pick_up=False,
                         description="A long bench, wide enough to fit around four people.")

    def interact(self, **kwargs):
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
    def use(self, item, player):
        destroyed_antimatter = False
        if item.name.title() == "Antimatter":
            print("With a swipe of the knife you cut open the antimatter. "
                  "A millisecond later you notice your mistake, just in time for "
                  "the world to collapse around you.")
            destroyed_antimatter = True
        if destroyed_antimatter:
            player.hp = 0
        else:  # Hits this if knife is used on something other than antimatter
            print("Nothing happens.")


class Food(Item):
    def __init__(self, name, description, eat_response="Tastes like chicken"):
        self.eat_response = eat_response
        super().__init__(name=name, description=description, can_pick_up=True)

    def eat(self):
        """
        Only prints the appropriate response (deletion of item is done in actions.py)
        """
        print(self.eat_response)


class Drink(Item):
    def __init__(self, name, description, drink_response="*gulp*"):
        self.drink_response = drink_response
        super().__init__(name=name, description=description, can_pick_up=True)

    def drink(self):
        print(self.drink_response)


class Tool(Item):
    def __init__(self, name, description, can_pick_up=True):
        super().__init__(name=name, description=description, can_pick_up=can_pick_up)

    def use(self, item, player):
        # Hammer can be used to break Terra Communications room lock
        if self.name.lower() == "hammer" and item.name.lower() == "lock":
            print("After a few blows, you are able to shatter the mechanical lock.")
            for i, item in enumerate(world.tile_exists(player.location_x, player.location_y).items):
                if item.name.lower() == "lock":
                    del world.tile_exists(player.location_x, player.location_y).items[i]  # Destroying lock
                    for location, tile in world._world.items():
                        if world.tile_exists(location[0], location[1]):
                            if tile.name == "Terra Communications Room":
                                tile.can_enter = True
                                break
        else:
            print("Nothing happens")
