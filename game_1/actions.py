"""
This module provides methods that are called and do a specific action that the user specifies they want to do.
"""
import world
from items import *  # BETTER WAY TO DO THIS?
from tiles import *  # BETTER WAY TO DO THIS?


def move(argument, player):
    """ Makes sure argument is connected and enter-able; moves player there if it is
    Args:
        argument (string): Capitalized user input past the first word
        player (player object): User's character's "player" object
        raw_argument (string): lowercase string of user argument of where to go
    Return:
        N/A but moves player as suggested or prints error
    """
    current_tile = world.tile_exists(player.location_x, player.location_y)
    if argument == "North":
        if world.tile_exists(player.location_x, player.location_y-1):
            new_tile = world.tile_exists(player.location_x, player.location_y-1)
            if new_tile.__class__.__name__ in current_tile.connected:  # Making sure prospective tile is connected
                if new_tile.can_enter:  # Making sure prospective tile is enter-able
                    player.move(player.location_x, player.location_y-1)
                else:
                    print(new_tile.name + " is locked.")
            else:
                print("You can't do that.")
        else:
            print("You can't do that.")
    elif argument == "South":
        if world.tile_exists(player.location_x, player.location_y+1):
            new_tile = world.tile_exists(player.location_x, player.location_y+1)
            if new_tile.__class__.__name__ in current_tile.connected:  # Making sure prospective tile is connected
                if new_tile.can_enter:  # Making sure prospective tile is enter-able
                    player.move(player.location_x, player.location_y+1)
                else:
                    print(new_tile.name + " is locked.")
            else:
                print("You can't do that.")
        else:
            print("You can't do that.")
    elif argument == "East":
        if world.tile_exists(player.location_x+1, player.location_y):
            new_tile = world.tile_exists(player.location_x + 1, player.location_y)
            if new_tile.__class__.__name__ in current_tile.connected:  # Making sure prospective tile is connected
                if new_tile.can_enter:  # Making sure prospective tile is enter-able
                    player.move(player.location_x+1, player.location_y)
                else:
                    print(new_tile.name + " is locked.")
            else:
                print("You can't do that.")
        else:
            print("You can't do that.")
    elif argument == "West":
        if world.tile_exists(player.location_x-1, player.location_y):
            new_tile = world.tile_exists(player.location_x-1, player.location_y)
            if new_tile.__class__.__name__ in current_tile.connected:  # Making sure prospective tile is connected
                if new_tile.can_enter:  # Making sure prospective tile is enter-able
                    player.move(player.location_x-1, player.location_y)
                else:
                    print(new_tile.name + " is locked.")
            else:
                print("You can't do that.")
        else:
            print("You can't do that.")
    else:
        print("Movement not recognized. Specify a cardinal direction.")
    return


def enter(player, argument, raw_argument):
    """ Makes sure argument is connected and enter-able; moves player there if it is
    Args:
        player (object): user's player object
        argument (string): Capitalized user input past the first word
        raw_argument (string): every word passed the first word of user input without modification
    Returns:
        N/A but changes user location to the new location if its in the list of connected locations to their current
        location.
    """
    if argument in world.tile_exists(player.location_x, player.location_y).connected:  # Making sure connected to current tile
        for location, tile in world._world.items():
            if tile.__class__.__name__ == argument:
                if tile.can_enter:  # Making sure new tile is enter-able
                    player.move(tile.x, tile.y)
                    return
                else:
                    print(tile.name + " is locked.")
                    return
                break
    else:
        print("Can't enter '" + raw_argument + "' from current location.")

    return


def interact_with(arguments, player):
    """ Action used for user input of "interact with _____"
    Args:
        arguments (list): List of capitalized strings of the third -> last words inputted by user (first=interact,
                          second=with)
        player (player object): User's character's "player" object
    Return:
        N/A but uses the player interacts with the specified item.
    """
    raw_item = " ".join(arguments)
    inputted_item = "".join(arguments)  # String of item to interact with (in correct class format)

    # Making sure item is in player's inventory or in the roo
    if inputted_item not in [item.__class__.__name__ for item in player.inventory]:
        if inputted_item not in [item.__class__.__name__ for item in
                        world.tile_exists(player.location_x, player.location_y).items]:
            print("'" + raw_item + "' not in your inventory or anywhere nearby.")
            return
    # Getting the actual item object
    else:  # WHAT IF THERE'S AN IDENTICALLY NAMED ITEM IN THE INVENTORY AND ROOM?
        for i, item in enumerate(player.inventory):
            if item.__class__.__name__ == inputted_item:
                player.inventory[i].interact()
                break
        for i, item in enumerate(world.tile_exists(player.location_x, player.location_y).items):
            if item.__class__.__name__ == inputted_item:
                world.tile_exists(player.location_x, player.location_y).items[i].interact()
                break
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
            break
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
                break
        for i, item in enumerate(world.tile_exists(player.location_x, player.location_y).items):
            if item.__class__.__name__ == item_2:
                item_2_index = i
                item_2_location = "room"
                break

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
        print("====================")
        print(item.name)
        print(item.description)
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
            world.tile_exists(player.location_x, player.location_y).items.append(item)
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
            if item.can_pick_up:
                player.inventory.append(item)  # Adds item to player inventory
                del items_in_room[index]  # Removes item from room
                print("Added " + raw_argument + " to your inventory.")
            else:
                print("You can't add that to your inventory.")
            return
    if raw_argument:
        print(
            "There is no '" + raw_argument + "' here.")  # Only gets here if there's none of specified item in inventory
    else:
        print("What do you want to pick up?")  # If no argument is specified
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
            print(item.description)
            return
    if raw_argument is not None:
        print(
            "There is no '" + raw_argument + "' here.")  # Only gets here if there's none of specified item in tile
    else:
        print("What do you want to examine?")
    return


def kill_player(player):
    """
    Args:
        player (object): user's player object
    Returns:
        N/A but kills player by setting their health to zero
    """
    player.hp = 0


def drink(player, argument, raw_argument):
    """
    Args:
        player (object): user's player object
        argument (string): Capitalized user input past the first word
        raw_argument (string): raw user argument
    Returns:
        N/A but drinks the argument
    """
    for index, item in enumerate(player.inventory):
        if item.name.lower() == argument.lower():
            if item.__class__.__name__ == "Drink":
                item.drink()
                del player.inventory[index]
                return
            else:
                print("I wouldn't drink that...")
                return
    for index, item in enumerate(world.tile_exists(player.location_x, player.location_y).items):
        if item.name.lower() == argument.lower():
            if item.__class__.__name__ == "Drink":
                item.drink()
                del world.tile_exists(player.location_x, player.location_y).items[index]
                return
            else:
                print("I wouldn't drink that...")
                return

    print("There's no '" + raw_argument + "' in your inventory or anywhere nearby.")
    return




    print("There's none of those in your inventory or anywhere nearby.")
    return
