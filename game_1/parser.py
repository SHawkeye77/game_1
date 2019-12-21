"""
This module takes a string of user input, finds its associated action, and calls that action.

Rules:
- User arguments should always be given as "<command> <argument_1> <argument_2> <etc...>"
- Users should enter actions one at a time
"""
import world
from items import *
import actions
import random

CONFUSED_RESPONSES = ["Come again?", "Sorry?", "Excuse me?", "Huh?", "What was that?"]


def parse_args(user_input, player):
    """
    Args:
        user_input (string): raw string of user input
        player (Player object): object of active player
    """
    # Accounting for null input
    if user_input.strip() == "":
        print(random.choice(CONFUSED_RESPONSES))
        return

    # Split string into list of strings (separated by spaces)
    list_of_input = user_input.split()
    # Splitting command into a verb and its following argument
    command = list_of_input[0].lower()
    if len(list_of_input) > 1:
        arguments = [x.lower() for x in list_of_input[1:]]  # Formatting each argument
        if command == "pick" and arguments[0] == "up":
            if len(arguments) > 1:
                actions.pick_up(player, "".join(arguments[1:]), " ".join(arguments[1:]))
            else:
                print("What do you want to pick up?")
            return
        elif command == "use" and ("on" in arguments):
            # Deals with "use ___ on ___ " input
            actions.use_on(arguments, player)
            return
        elif command == "interact" and (arguments[0] == "with"):
            # Deals with "interact with _____ " input
            if len(arguments) < 2:  # If user just says "interact with"
                print("Specify what you'd like to interact with.")
            else:
                actions.interact_with(arguments[1:], player)
            return
        raw_argument = " ".join(list_of_input[1:])  # Here's the raw argument
        argument = (" ".join(arguments))  # Turning into name format.
    else:
        argument = ""
        raw_argument = ""

    if command == "go" or command == "move":
        actions.move(argument, player)
    elif command in ["east", "west", "north", "south"]:
        actions.move(command, player)
    elif command == "observe" and argument == "" or command == "look" and (argument == "around" or argument == ""):
        actions.examine_surroundings(player)
    elif command == "inventory" or (command == "view" and argument == "inventory") or (command == "i" and argument==""):
        actions.print_inventory(player)
    elif command == "where" and argument == "am i" or (command == "location" and argument == ""):
        actions.where(player)
    elif command == "drop":
        actions.drop(player, argument, raw_argument)
    elif command == "grab" or command == "take" or command == "get":
        actions.pick_up(player, argument, raw_argument)
    elif command == "examine":
        actions.examine(player, arguments, raw_argument)
    elif command == "enter":
        actions.enter(player, argument, raw_argument)
    elif (command == "kill" and argument == "myself") or (command == "kms"):
        actions.kill_player(player)
    elif command == "drink":
        actions.drink(player, argument, raw_argument)
    elif command == "eat":
        actions.eat(player, argument, raw_argument)
    elif command == "uuddlrlrbastart":  # Konami code
        print("Nice try, bud.")
    else:
        print(random.choice(CONFUSED_RESPONSES))

    return

