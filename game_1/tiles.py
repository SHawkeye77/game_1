"""
This module has the core "Location" class as well as imports all tile classes from "tiles_all" directory
"""


class Location:
    """ Template for a single location/tile. All places must derive from this """
    def __init__(self, x, y, name, description, items=[], can_enter=True, been_entered=False, connected=[]):
        self.x = x  # X-Coordinate of the location (should never be directly seen by player)
        self.y = y  # Y-Coordinate of the location (should never be directly seen by player)
        self.items = items  # List of objects (items) at this location
        self.name = name  # String name of the location (not list like items)
        self.description = description  # Description of the location
        self.can_enter = can_enter  # True if its enter-able, false if locked (or otherwise not enter-able)
        self.been_entered = been_entered  # False if room has never been entered by the player
        self.connected = connected  # List of strings corresponding to all names of connected
                                    # locations (in appropriate class-name (NOT class.name) format)

    def first_entrance(self):
        """ Is run only if it's the user's first time entering this location """
        print("Location: " + self.name + "\n" + self.description)


# These are imported so that any file importing "tiles.py" can have access to all tiles classes
from tiles_all.tiles_landing_dome import *
from tiles_all.tiles_main_dome import *
