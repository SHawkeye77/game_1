"""
This module provides methods that are called and do a specific action that the user specifies they want to do.
"""
import world
import items  # BETTER WAY TO DO THIS?
from tiles import *  # BETTER WAY TO DO THIS?


def move(argument, player):
    """ Makes sure argument is connected and enter-able; moves player there if it is
    Args:
        argument (string): lowercase user input of direction
        player (player object): User's character's "player" object
    Return:
        N/A but moves player as suggested or prints error
    """
    current_tile = world.tile_exists(player.location_x, player.location_y)
    if argument == "north":
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
    elif argument == "south":
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
    elif argument == "east":
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
    elif argument == "west":
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
        argument (string): lowercase user input past the first word
        raw_argument (string): every word passed the first word of user input without modification
    Returns:
        N/A but changes user location to the new location if its in the list of connected locations to their current
        location.
    """
    new_arg = argument.title().replace(" ", "")
    if new_arg in world.tile_exists(player.location_x, player.location_y).connected:  # Making sure connected to current tile
        for location, tile in world._world.items():
            if tile.__class__.__name__ == new_arg:
                if tile.can_enter:  # Making sure new tile is enter-able
                    player.move(tile.x, tile.y)
                    return
                else:
                    print(tile.name + " is locked.")
                    return
    else:
        print("Can't enter '" + raw_argument + "' from current location.")

    return


def interact_with(arguments, player):
    """ Action used for user input of "interact with _____"
    Args:
        arguments (list): List of lowercase strings of the 3rd -> last words inputted by user (first=interact,
                          second=with)
        player (player object): User's character's "player" object
    Return:
        N/A but uses the player interacts with the specified item.
    """
    inputted_item = " ".join(arguments)
    current_loc = world.tile_exists(player.location_x, player.location_y)
    # If it's in player inventory
    if inputted_item in [item.name.lower() for item in player.inventory]:
        for i, item in enumerate(player.inventory):
            if inputted_item in [name.lower() for name in item.name]:
                player.inventory[i].interact(player)
                return
    # If it's in the room
    elif inputted_item in [item.name.lower() for item in current_loc.items]:
        for i, item in enumerate(current_loc.items):
            if inputted_item in [name.lower() for name in item.name]:
                current_loc.items[i].interact(player)
                return
    # If it's not in inventory or room
    else:  # WHAT IF THERE'S AN IDENTICALLY NAMED ITEM IN THE INVENTORY AND ROOM?
        print("'" + inputted_item + "' not in your inventory or anywhere nearby.")
    return


def use_on(arguments, player):
    """ Action used for user input of "use ___ on ___"
    Args:
        arguments (list): List of lowercase strings of the second -> last words inputted by user.
        player (player object): User's character's "player" object
    Return:
        N/A but uses the suggested item 1 on suggested item 2
    """

    for i, arg in enumerate(arguments):
        if arg == "on":
            index_of_on = i
            break
    item_1 = " ".join(arguments[:index_of_on])  # String of item_1 in name format
    item_2 = " ".join(arguments[index_of_on + 1:])  # String of item_2 in name format

    # Gathering and finding item names
    inventory_names = []  # All possible names for items in inventory
    room_names = []  # All possible names for items in the room
    for item in player.inventory:
        inventory_names += item.name
    for item in world.tile_exists(player.location_x, player.location_y).items:
        room_names += item.name

    # Making sure first item is in player's inventory
    if item_1 not in [item.lower() for item in inventory_names]:
        print("'" + item_1 + "' not in your inventory.")
        return

    # Gets actual item_1 object
    else:
        for i, item in enumerate(player.inventory):
            if item_1 in [name.lower() for name in item.name]:
                item_1_index = i
                break

    # Making sure second item is in player's inventory or in the room
    if item_2 not in [item.lower() for item in inventory_names]:
        if item_2 not in [item.lower() for item in room_names]:
            print("'" + item_2 + "' not in your inventory or anywhere nearby.")
            return

    # Getting the actual item_2 object (only reaches here if it is in room or inventory)
    # WHAT IF THERE'S AN IDENTICALLY NAMED ITEM IN THE INVENTORY AND ROOM?
    for i, item in enumerate(player.inventory):
        if item_2 in [name.lower() for name in item.name]:
            item_2_index = i
            item_2_location = "inventory"
            break
    for i, item in enumerate(world.tile_exists(player.location_x, player.location_y).items):
        if item_2 in [name.lower() for name in item.name]:
            item_2_index = i
            item_2_location = "room"
            break

    # Calling the associated "use" function with the correct objects
    if item_2_location == "inventory":
        player.inventory[item_1_index].use(player.inventory[item_2_index], player)
    elif item_2_location == "room":
        player.inventory[item_1_index].use(
            world.tile_exists(player.location_x, player.location_y).items[item_2_index], player)
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
    print("\nInventory:")
    if len(player.inventory) >= 1:
        for item in player.inventory:
            print(item.name[0].title())
            print(" -> " + item.description)
    else:
        print("You have nothing in your inventory.")
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
        if argument in [name.lower() for name in item.name]:
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
        argument (string): lowercase user input past the first word
        raw_argument (string): every word passed the first word of user input without modification
    Returns:
        N/A but adds argument from tile's items to current player's inventory
    """
    items_in_room = world.tile_exists(player.location_x, player.location_y).items
    for index, item in enumerate(items_in_room):
        if argument in [name.lower() for name in item.name]:
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
        argument (string): lowercase user input past the first word
        raw_argument (string): every word passed the first word of user input without modification
    Returns:
        N/A but prints description of user specified item if its in the current tile
    """
    items_in_room = world.tile_exists(player.location_x, player.location_y).items
    for index, item in enumerate(items_in_room):
        if argument in [name.lower() for name in item.name]:
            print(item.description)
            return
    if raw_argument is not "":
        print(
            "There is no '" + raw_argument + "' in the room.")  # Only gets here if none of specified item are in tile
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
        argument (string): lowercase user input past the first word
        raw_argument (string): raw user argument
    Returns:
        N/A but drinks the argument
    """
    for index, item in enumerate(player.inventory):
        if argument in [name.lower() for name in item.name]:
            if isinstance(item, items.Drink):
                item.drink()
                del player.inventory[index]
                return
            else:
                print("I wouldn't drink that...")
                return
    for index, item in enumerate(world.tile_exists(player.location_x, player.location_y).items):
        if argument in [name.lower() for name in item.name]:
            if isinstance(item, items.Drink):
                item.drink()
                del world.tile_exists(player.location_x, player.location_y).items[index]
                return
            else:
                print("I wouldn't drink that...")
                return

    print("There's no '" + raw_argument + "' in your inventory or anywhere nearby.")
    return


def eat(player, argument, raw_argument):
    """
    Args:
        player (object): user's player object
        argument (string): lowercase user input past the first word
        raw_argument (string): raw user argument
    Returns:
        N/A but drinks the argument
    """
    for index, item in enumerate(player.inventory):
        if argument in [name.lower() for name in item.name]:
            if isinstance(item, items.Food):
                item.eat()
                del player.inventory[index]
                return
            else:
                print("I wouldn't eat that...")
                return
    for index, item in enumerate(world.tile_exists(player.location_x, player.location_y).items):
        if argument in [name.lower() for name in item.name]:
            if isinstance(item, items.Food):
                item.eat()
                del world.tile_exists(player.location_x, player.location_y).items[index]
                return
            else:
                print("I wouldn't eat that...")
                return

    print("There's no '" + raw_argument + "' in your inventory or anywhere nearby.")
    return
