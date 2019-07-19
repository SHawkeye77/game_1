"""
This module holds scenarios that the player can go through.
"""
import world
import items


def detox_room_entrance():
    """
    Plays the scenario that happens when you enter the detox room immediately upon landing
    """
    print("Upon entering the chamber you're blasted by fans. It's warm air but with what feels like "
          "specks of sand in it.\nAfter a minute or so it stops. From the speaker above, "
          "a voice greets you...\n"
          "\"Welcome to the UNEEA Martian base! We hope your stay is exciting and thoroughly informative.\"")

    for location, tile in world._world.items():
        if tile.__class__.__name__ == "IntegrationRoom":
            int_room=tile

    while True:
        user_input = input("\"Can I get you a beverage?\" ")
        list_of_input = user_input.lower().split()
        if "coffee" in list_of_input and ("not" not in list_of_input):
            int_room.items.append(items.Coffee())
            break
        elif "tea" in list_of_input and ("not" not in list_of_input):
            int_room.items.append(items.Tea())
            break
        elif "water" in list_of_input and ("not" not in list_of_input):
            int_room.items.append(items.Water())
            break
        elif "pepsi" in list_of_input and ("not" not in list_of_input):
            print("I'm sorry, we only have Coke, I hope that's okay!")
            int_room.items.append(items.Coke())
            return
        elif lists_overlap(["pop", "soda", "coke"], list_of_input) and ("not" not in list_of_input):
            int_room.items.append(items.Coke())
            break
        elif lists_overlap(["beer", "vodka", "rum", "martini", "alcohol", "tequila", "wine", "booze"], list_of_input)\
                and ("not" not in list_of_input):
            print("\"We would rather your mind stay sharp during your visit.\"")
        elif "nothing" in list_of_input and ("not" not in list_of_input):
            print("\"We would prefer you stay hydrated during your visit.\"")
        else:
            print("\"I'm sorry, I don't understand.\"")

    print("\"Great choice. We will have it ready for you right away.\"")


def lists_overlap(a, b):
    """ Returns true if list 'a' and list 'b' have overlap """
    return bool(set(a) & set(b))
