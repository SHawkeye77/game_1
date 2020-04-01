"""
Holds items specifically made in the landing dome
"""

from items import Item
from items_all.items_general import *

################################# TCR Items #################################
class TcrLock(Item):
    def __init__(self):
        super().__init__(name=["Lock", "TCR Lock"], can_pick_up=False,
                         description="An old, bulky, mechanical lock.")

class APMPass(Item):
    def __init__(self):
        super().__init__(name=["Key Card"],
                         description="It's dark-blue and looks like a credit-card.")

    def use(self, item, player):
        if "tablet" in [name.lower() for name in item.name]:
            print("*click*")
            print("From a speaker above, you're greeted by a familiar voice...")
            scenarios.apm_terminal(player)
        else:
            print("Nothing happens.")

class DeadCommunicationsDirector(Item):
    def __init__(self):
        super().__init__(name=["Communications Director", "Corpse"], can_pick_up=False,
            description="It is clear something awful happened to the director.\n"
                "His skin is, for the most part, torn. While some tears look like cuts, others "
                "are large enough to expose patches of his anatomy underneath... "
                "The intact portions of the man's skin are not normal either; at these spots "
                "the skin has clumped together and begun to sag from the man's body. "
                "There seems to be a note, as well as what looks like a small key card poking out "
                "of his breast pocket.")

    def interact(self, player):
        print("Yeah right, no way I'm touching that.")

class Transmitter(Item):
    def __init__(self):
        super().__init__(name=["Transmitter"], can_pick_up=False,
                         description="A metallic, tapering cylinder pointing up towards the sky. In the center you "
                                     "can see its photopropulsion apparatus. Looks like it's been tampered with...")

class Note(Item):
    """ A slip of paper with info on it """
    def __init__(self, description):
        super().__init__(name=["Note"], description=description)

########################### Integration Room Items ###########################
class Plant(Item):
    def __init__(self):
        super().__init__(name=["Plant", "Potted Plant"],
                         description="Looks like a Ficus Danielle, similar-looking to one at your apartment on Terra. "
                                     "It's clearly fake.")

################################ Garage Items ################################
class Rover(Item):
    def __init__(self, locked=True, player_inside=False):
        self.locked = locked
        self.player_inside = player_inside  # True if the player is inside and piloting the rover
        super().__init__(name=["Rover"], can_pick_up=False,
                         description="A modest rover. The cabin is tube-shaped, and there's four huge wheels"
                                     " jutting out from each side.")

    def interact(self, player): # TODO: TO BE EXPANDED ON (OBVIOUSLY)
        if self.locked:
            print("It's locked. Looks like it requires a key-code to enter.")
        else:
            print("It's unlocked! You climb inside.")
            self.player_inside = True  # MAKE SURE WHEN YOU LEAVE ROVER THIS SWITCHES BACK TO FALSE!


class GarageLever(Item):
    # This lever controls opening/closing the garage bay door
    def __init__(self, garage_down=True):
        self.garage_down = garage_down
        super().__init__(name=["Lever"], can_pick_up=False,
                         description="A bulky mechanical lever. There's a wire attached to it that follows the "
                                     "dome above and ends at the garage door.")

    def interact(self, player):
        scenarios.opened_garage(player, self)
