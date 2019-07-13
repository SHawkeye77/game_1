"""
This module provides methods that are called and do a specific action that the user specifies they want to do.
"""
import world
from items import *

def move(argument, player):
    """ Action used for user input of "use ___ on ___"
    Args:
        argument (string): Capitalized user input past the first word
        player (player object): User's character's "player" object
    Return:
        N/A but moves player as suggested or prints error
    """
    if argument == "North":
        player.move(0, -1)
    elif argument == "South":
        player.move(0, 1)
    elif argument == "East":
        player.move(1, 0)
    elif argument == "West":
        player.move(-1, 0)
    else:
        print("Movement not recognized. Specify a cardinal direction.")
    return


def use_on(arguments, player):
    """ Action used for user input of "use ___ on ___"
    Args:
        arguments (list): List of capitalized strings of the second -> last words inputted by user.
        player (player object): User's character's "player" object
    Return:
        N/A but uses the suggested item 1 on suggested item 2
    """
    for i, arg in enumerate(arguments):
        if arg == "On":
            index_of_on = i
    item_1 = "".join(arguments[:index_of_on])  # String of item_1 in correct class format
    item_2 = "".join(arguments[index_of_on + 1:])  # String of item_2 in correct class format
    raw_item_1 = " ".join(arguments[:index_of_on])
    raw_item_2 = " ".join(arguments[index_of_on + 1:])
    # Making sure first item is in player's inventory
    if item_1 not in [item.__class__.__name__ for item in player.inventory]:
        print("'" + raw_item_1 + "' not in your inventory.")
        return
    # Gets actual item_1 object
    else:
        for i, item in enumerate(player.inventory):
            if item.__class__.__name__ == item_1:
                item_1_index = i
    # Making sure second item is in player's inventory or in the room
    if item_2 not in [item.__class__.__name__ for item in player.inventory]:
        if item_2 not in [item.__class__.__name__ for item in
                          world.tile_exists(player.location_x, player.location_y).items]:
            print("'" + raw_item_2 + "' not in your inventory or anywhere nearby.")
            return
    # Getting the actual item_1 object
    else:  # WHAT IF THERE'S AN IDENTICALLY NAMED ITEM IN THE INVENTORY AND ROOM?
        for i, item in enumerate(player.inventory):
            if item.__class__.__name__ == item_2:
                item_2_index = i
                item_2_location = "inventory"
        for i, item in enumerate(world.tile_exists(player.location_x, player.location_y).items):
            if item.__class__.__name__ == item_2:
                item_2_index = i
                item_2_location = "room"

    # Calling the associated "use" function with the correct objects
    if item_2_location == "inventory":
        player.inventory[item_1_index].use(player.inventory[item_2_index])
    elif item_2_location == "room":
        player.inventory[item_1_index].use(
            world.tile_exists(player.location_x, player.location_y).items[item_2_index])
    return


def examine_surroundings(player):
    """
    Args:
        player (object): user's player object
    returns:
        N/A but prints description of current tile of the player
    """
    print(world.tile_exists(player.location_x, player.location_y).description)
    return


def where(player):
    """
    Args:
        player (object): user's player object
    returns:
        N/A but prints name of current room
    """
    print("Location: " + world.tile_exists(player.location_x, player.location_y).name)
    return


def print_inventory(player):
    """
    Args:
        player (object): user's player object
    returns:
        N/A but prints each item in player's inventory
    """
    for item in player.inventory:
        print(item, end='\n')
    return


def drop(player, argument, raw_argument):
    """
    Args:
        player (object): user's player object
        argument (string): Capitalized user input past the first word
        raw_argument (string): every word passed the first word of user input without modification
    Returns:
        N/A but adds argument from player inventory to current tile's items
    """
    for index, item in enumerate(player.inventory):
        if item.__class__.__name__ == argument:
            world.tile_exists(player.location_x, player.location_y).items.append(eval(argument)())
            del player.inventory[index]
            print("You drop your " + raw_argument + ".")
            return
    print("You don't have one of those!")  # Only gets here if there's none of specified item in inventory
    return


def pick_up(player, argument, raw_argument):
    """
    Args:
        player (object): user's player object
        argument (string): Capitalized user input past the first word
        raw_argument (string): every word passed the first word of user input without modification
    Returns:
        N/A but adds argument from tile's items to current player's inventory
    """
    items_in_room = world.tile_exists(player.location_x, player.location_y).items
    for index, item in enumerate(items_in_room):
        if item.__class__.__name__ == argument:
            player.inventory.append(eval(argument)())  # Adds item to player inventory
            del items_in_room[index]  # Removes item from room
            print("Added " + raw_argument + " to your inventory.")
            return
    if raw_argument:
        print(
            "There is no '" + raw_argument + "' here.")  # Only gets here if there's none of specified item in inventory
    else:
        print("What do you want to pick up?")
    return


def examine(player, argument, raw_argument):
    """
    Args:
        player (object): user's player object
        argument (string): Capitalized user input past the first word
        raw_argument (string): every word passed the first word of user input without modification
    Returns:
        N/A but prints description of user specified item if its in the current tile
    """
    items_in_room = world.tile_exists(player.location_x, player.location_y).items
    for index, item in enumerate(items_in_room):
        if item.__class__.__name__ == argument:
            print(eval(argument)().description)  # Describes specified
            return
    if raw_argument is not None:
        print(
            "There is no '" + raw_argument + "' here.")  # Only gets here if there's none of specified item in tile
    else:
        print("What do you want to examine?")
    return

