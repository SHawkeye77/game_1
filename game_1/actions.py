"""
This module basically maps hotkeys/easily-called-methods to player actions.
"""

from player import Player  # might just be import Player???


class Action:
    def __init__(self, method, name, hotkey, **kwargs):
        # All actions will have a name, hotkey, and associated method, but we have possibility for more with **kwargs
        self.method = method  # The associated method for the action
        self.name = name  # Name of the action
        self.hotkey = hotkey  # Hotkey you want to bind to the action
        self.kwargs = kwargs  # Any additional arguments that will be needed by the method self.method

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)


class Flee(Action):
    def __init__(self, tile):
        super().__init__(method=Player.flee, name="Flee", hotkey='f', tile=tile)


class MoveNorth(Action):
    """ Moves player north """
    def __init__(self):
        # Note: move_north not move_north() because we reference the method but don't want to actually call it
        super().__init__(method=Player.move_north, name='Move north', hotkey='n')


class MoveSouth(Action):
    """ Moves player south """
    def __init__(self):
        super().__init__(method=Player.move_south, name='Move south', hotkey='s')


class MoveEast(Action):
    """ Moves player east """
    def __init__(self):
        super().__init__(method=Player.move_east, name='Move east', hotkey='e')


class MoveWest(Action):
    """ Moves player west """
    def __init__(self):
        super().__init__(method=Player.move_west, name='Move west', hotkey='w')


class ViewInventory(Action):
    """ Prints the player's inventory """
    def __init__(self):
        super().__init__(method=Player.print_inventory, name='View inventory', hotkey='i')


class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=Player.attack, name="Attack", hotkey='a', enemy=enemy)

class KillPlayer(Action):
    def __init__(self):
        super().__init__(method=Player.mod_hp, name="Kill Player",hotkey='k',amount=-100)