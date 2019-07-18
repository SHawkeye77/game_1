"""
This module holds scenarios that the player can go through.
"""
import world
from items import Drink


def detox_room_entrance():
    """
    Plays the scenario that happens when you enter the detox room immediately upon landing
    """
    print("Upon entering the chamber you're blasted by fans. It's warm air but with what feels like "
          "specks of sand in it.\nAfter a minute or so it stops. From the speaker above, "
          "a voice greets you...\n"
          "\"Welcome to the UNEEA Martian base! We hope your stay is exciting and thoroughly informative\"")

    for location, tile in world._world.items():
        if tile.__class__.__name__ == "IntegrationRoom":
            int_room=tile

    while True:
        user_input = input("\"Can I get you a beverage?\" ")
        list_of_input = user_input.lower().split()

        if "coffee" in list_of_input and "not" not in list_of_input:
            int_room.items.append(Drink(name="cup of coffee", description="Looks like dark roast."))
            break
        elif "tea" in list_of_input and "not" not in list_of_input:
            int_room.items.append(Drink(name="glass of tea", description="A small glass of herbal tea."))
            break
        elif "water" in list_of_input and "not" not in list_of_input:
            int_room.items.append(Drink(name="glass of water", description="A large glass of water."))
            break
        elif "pepsi" in list_of_input and "not" not in list_of_input:
            print("I'm sorry, we only have Coke, I hope that's okay!")
            int_room.items.append(Drink(name="can of Coke", description="It's a normal can of Coke."))
        elif "pop" or "soda" or "coke" in list_of_input and "not" not in list_of_input:
            int_room.items.append(Drink(name="Coke", description="It's a normal can of Coke."))
            break
        elif "beer" or "vodka" or "rum" or "martini" or "tequila" or "wine"\
                in list_of_input and "not" not in list_of_input:
            print("\"We would rather your mind stay sharp for your stay.\"")
        elif "nothing" in list_of_input and "not" not in list_of_input:
            print("\"We would prefer you stay hydrated during your visit.\"")
        else:
            print("\"I'm sorry, I don't understand.\"")

    print("\"Great choice. We will have it ready for you right away.\"")

#JDSKLF:DJSFJDL:JSDKLF:DJSFKL:DFS
#DEFAULTS TO COKE AND DOESNT ADD IT TO THE ROOM
#JDSKLF:DJSFJDL:JSDKLF:DJSFKL:DFS