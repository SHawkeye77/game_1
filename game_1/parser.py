"""
This module takes a string of user input, finds its associated action, and calls that action.

Rules:
- User arguments should always be given as "<command> <argument_1> <argument_2> <etc...>"
- Users should enter actions one at a time
"""
import world
from items import *
import actions


def parse_args(user_input, player):
    """
    Args:
        user_input (string): raw string of user input
        player (Player object): object of active player
    """
    # Accounting for null input
    if user_input.strip() == "":
        return

    # Split string into list of strings (separated by spaces)
    list_of_input = user_input.split()
    # Splitting command into a verb and its following argument
    command = list_of_input[0].lower()
    if len(list_of_input) > 1:
        arguments = [x.lower().title() for x in list_of_input[1:]]  # Formatting each argument
        if command == "pick" and arguments[0] == "Up":
            if len(arguments) > 1:
                actions.pick_up(player, "".join(arguments[1:]), " ".join(arguments[1:]))
            else:
                print("What do you want to pick up?")
            return
        elif command == "use" and ("On" in arguments):
            # Deals with "use ___ on ___ " input
            actions.use_on(arguments, player)
            return
        elif command == "interact" and (arguments[0] == "With"):
            # Deals with "interact with _____ " input
            if len(arguments) < 2:  # If user just says "interact with"
                print("Specify what you'd like to interact with.")
            else:
                actions.interact_with(arguments[1:], player)
            return
        raw_argument = " ".join(list_of_input[1:])  # Here's the raw argument
        argument = "".join(arguments)  # Turning into un-spaced argument. Example: "FirstSecondThird"
    else:
        argument = None
        raw_argument = None

    if command == "go" or command == "move":
        actions.move(argument, player)
    elif command == "observe" or command == "look":
        actions.examine_surroundings(player)
    elif command == "inventory" or (command == "view" and argument == "Inventory"):
        actions.print_inventory(player)
    elif command == "where" and argument == "AmI":
        actions.where(player)
    elif command == "drop":
        actions.drop(player, argument, raw_argument)
    elif command == "grab" or command == "take" or command == "get":
        actions.pick_up(player, argument, raw_argument)
    elif command == "examine":
        actions.examine(player, argument, raw_argument)
    elif command == "enter":
        actions.enter(player, argument, raw_argument)
    elif command == "kill" and argument == "Myself":
        actions.kill_player(player)

    else:
        print("Command not recognized.")

    return

