"""
This module has the core "Item" class as well as imports all items classes from "items_all" directory

Items classes should always follow the format:
Capital letters for the start of new words.
Examples: Book, GarageDoor, ElectricalCable, etc.

NOTE: If an item description has multiple lines, each line after the first should start with a "\t" (tab)
NOTE: Items are interacted with by their associated item.name attribute. It should be intuitive to the player.
NOTE: Items must be able to accept player for all "use" overrides, and player for all "interact" overrides.
"""

import scenarios
import world


class Item:
    """ Base class for all items """
    def __init__(self, name, description, can_pick_up=True):
        self.name = name  # List of names for item (any of which can be used to reference it). First one should be main.
        self.description = description  # Description of item
        self.can_pick_up = can_pick_up  # Can the user add this to their inventory

    def use(self, item, player):
        """
        Used for "use _____ on _____" input
        Call when you want to use the current (self) item on the item that is passed in (in overridden methods of use).
        e.g. use key on door

        Args:
            item (list of objects): other item we are going to use the current (self) item on.
            player (object): current user's player object
        Returns:
            N/A but uses self object on item object
        """
        # Override in child class if you want to have the object able to be used on something
        print("Nothing happens.")

    def interact(self, player):
        """
        Used for "interact with _____" input
        Call when you want to interact with the current (self) item
        e.g. interact with door
        """
        # Override in child class if you want to have the object interact-able
        print("Nothing happens.")


# By importing all these, file can have access to all items by simply
# including this one. The below files each import items_general.py (so it's
# not included here)
from items_all.items_landing_dome import *
from items_all.items_main_dome import *
from items_all.items_research_dome import *
