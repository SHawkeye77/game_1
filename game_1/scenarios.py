"""
This module holds scenarios that the player can go through.
"""
import world
import items
from resources import lore


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
            int_room = tile

    while True:
        user_input = input("\"Can I get you a beverage?\" ")
        list_of_input = user_input.lower().split()
        if "coffee" in list_of_input and ("not" not in list_of_input):
            int_room.items.append(items.Drink(name=["Coffee"], description="Looks like dark roast.",
                                              drink_response="\n*gulp*\nIt's hot but tasty. "
                                                             "Could've used some cream in it though..."))
            break
        elif "tea" in list_of_input and ("not" not in list_of_input):
            int_room.items.append(items.Drink(name=["Tea"], description="A small glass of herbal tea.",
                                              drink_response="\n*gulp*\nIt's warm but tasty. "
                                                             "Could've used some honey in it though..."))
            break
        elif "water" in list_of_input and ("not" not in list_of_input):
            int_room.items.append(items.Drink(name=["Water"], description="A large glass of water.",
                                  drink_response="\n*gulp*\nNothing like a cold glass of water.\n"))
            break
        elif "pepsi" in list_of_input and ("not" not in list_of_input):
            print("I'm sorry, we only have Coke, I hope that's okay!")
            int_room.items.append(items.Drink(name=["Coke"], description="It's a normal can of Coke.",
                                  drink_response="\n*gulp*\nJust like Terran Coke"))
            return
        elif lists_overlap(["pop", "soda", "coke"], list_of_input) and ("not" not in list_of_input):
            int_room.items.append(items.Drink(name=["Coke"], description="It's a normal can of Coke.",
                                  drink_response="\n*gulp*\nJust like Terran Coke"))
            break
        elif lists_overlap(["beer", "vodka", "rum", "martini", "alcohol", "tequila", "wine", "booze"], list_of_input)\
                and ("not" not in list_of_input):
            print("\"We would rather your mind stay sharp during your visit.\"")
        elif "nothing" in list_of_input and ("not" not in list_of_input):
            print("\"We would prefer you stay hydrated during your visit.\"")
        elif "yes" in list_of_input or "sure" in list_of_input:
            print("\"Great! What can I get you?\"")
        else:
            print("\"I'm sorry, I don't understand.\"")

    print("\"Great choice. We will have it ready for you right away.\"")


def lists_overlap(a, b):
    """ Returns true if list 'a' and list 'b' have overlap """
    return bool(set(a) & set(b))


def opened_garage(player, lever):
    """ Plays scenario that happens when pressing the lever

    Returns:
         True if garage is shut immediately, False otherwise.
    """
    # Getting the rover object (so we can see if player is inside)
    for index, item in enumerate(world.tile_exists(player.location_x, player.location_y).items):
        if "rover" in [name.lower() for name in item.name]:
            rover = item

    if lever.garage_down:
        lever.garage_down = False
        if rover.player_inside:  # If player triggers lever from inside the rover
            print("From the safety of the rover, you see the garage door rise to the ceiling, "
                  "exposing the Martian environment outside...")
        else:  # If player pulls lever from out in the open
            print("The heavy lever creaks upwards. Behind you, the garage bay door creaks "
                  "and begins to open. Before you even have time to think about what you just did, "
                  "your body cools rapidly. You gasp for air, unsuccessfully.")
            user_input = input("What do you do? ")
            list_of_input = user_input.lower().split()
            if "lever" in list_of_input:  # Player must
                # Run if player immediately shuts garage upon their mistake
                print("Even as the world turns hazy around you, you muster the strength to lean into the lever, "
                      "pressing it upwards. The garage door slams shut behind you as recover your breath...")
                lever.garage_down = True
            else:
                print("It's no use.")
                player.hp = 0  # Kills the player
    else:
        print("The lever falls downwards and the garage door returns to a closed position.")
        lever.garage_down = True


def computer_usage(player):
    """ The scenario for when the player interacts with a secure computer. """
    print("Type 'exit' at any time to leave the computer.")
    first_time_login = True
    while True:
        if first_time_login:
            first_time_login = False
            print("\n" + lore.GUI_LOGIN)
        else:
            print("\n" + lore.GUI_LOGIN_AFTER_FAIL)
        username = input("What 'USERNAME' do you enter? ")
        if username.lower() == "exit":
            print("You exit out of the computer.")
            return
        password = input("What 'PASSWORD' do you enter? ")
        if username == "luxxx825" and password == "gellerfan334!":
            computer_usage_communications_director()
            return
        elif password.lower() == "exit":
            print("You exit out of the computer.")
            return


def computer_usage_communications_director():
    """ If the communications director logs into a computer, it goes here. """
    from_messages = False
    print(lore.COMM_DIR_POST_LOGIN_GUI)
    while True:
        if from_messages:
            print(lore.COMM_DIR_POST_LOGIN_GUI)
            from_messages=False
        clicked = input("What do you click? ").lower()

        # Sent messages
        if clicked == "view sent messages" or clicked == "sent messages":
            print(lore.COMM_DIR_SENT_MESSAGES)
            while True:
                clicked = input("What do you click? ").lower()
                if clicked == "back":
                    from_messages = True
                    break  # Goes back to login gui
                elif clicked == "exit":
                    print("You log out of the computer.")
                    return
                else:
                    print("Not an available option...")

        # Drafts page
        elif clicked == "view drafts" or clicked == "drafts":
            print(lore.COMM_DIR_DRAFTS)
            while True:
                clicked = input("What do you click? ").lower()
                if clicked == "back":
                    from_messages = True
                    break  # Goes back to login gui
                elif clicked == "exit":
                    print("You log out of the computer.")
                    return
                else:
                    print("Not an available option...")

        elif clicked == "exit":
            print("You log out of the computer.")
            return
        else:
            print("Not an available option...")


def apm_terminal(player):
    """ Plays the scenario for the player choosing a place to go from the terminal (starting from greeting)
    Args:
        player (object): Player object of current player (needed for current location)
    Returns:
         N/A but interacts with the player to select a viable location, then transports them there.
    """
    # Getting the objects of the 4 terminals
    for location, tile in world._world.items():
        if world.tile_exists(location[0], location[1]):
            if tile.name == "APM Terminal A":
                terminal_a = tile
            elif tile.name == "APM Terminal B":
                terminal_b = tile
            elif tile.name == "APM Terminal C":
                terminal_c = tile
            elif tile.name == "APM Terminal D":
                terminal_d = tile

    current_terminal = world.tile_exists(player.location_x, player.location_y).name
    available_options = []
    if current_terminal == "APM Terminal A":
        available_options += ["Terminal B"]
    elif current_terminal == "APM Terminal B":
        available_options += [""]
    elif current_terminal == "APM Terminal C":
        available_options += [""]
    elif current_terminal == "APM Terminal D":
        available_options += [""]
    available_options += ["Remain Here", "What Is This"]

    been_entered = False
    while True:
        if been_entered:
            print("\"Where would you like to go?\"\n\"Please specify one of the following options:\" ")
        else:
            # It says Mr. Lu because you are using his key card.
            print("\"Hello Mr.Lu! Welcome to the APM transportation interface.\"\n"
                  "\"Where would you like to go?\"\n\"Please specify one of the following options:\"")
            been_entered = True
        for option in available_options:
            print(" - \"" + option + "\"")
        user_input = input("")
        to_go = user_input.strip().lower()
        if to_go == "terminal a" and "Terminal A" in available_options:
            print("\"Sounds great! We will send a tram to your location right away. Safe travels!\"")
            print("Less than a minute later, a two-car tram arrives at the tracks in front of you. You step in, "
                  "the doors are sealed, and you're transported through a tubed environment to the Landing "
                  "Dome's Terminal A ...")
            player.move(terminal_a.x, terminal_a.y)
            return
        elif to_go == "terminal b" and "Terminal B" in available_options:
            print("\"Sounds great! We will send a tram to your location right away. Safe travels!\"")
            print("Less than a minute later, a two-car tram arrives at the tracks in front of you. You step in, "
                  "the doors are sealed, and you're transported through a tubed environment to the Main Dome's "
                  "Terminal B...")
            player.move(terminal_b.x, terminal_b.y)
            return
        elif to_go == "terminal c" and "Terminal C" in available_options:
            print("\"Sounds great! We will send a tram to your location right away. Safe travels!\"")
            print("CODE IN THE PLAYER GOING TO TERMINAL C")
            return
        elif to_go == "terminal d" and "Terminal D" in available_options:
            print("\"Sounds great! We will send a tram to your location right away. Safe travels!\"")
            print("CODE IN THE PLAYER GOING TO TERMINAL D")
            return
        elif to_go == "earth":
            print("Well, aren't you clever")
        elif to_go == "remain here":
            print("\"Understood. We will not send a tram to your location. Have a wonderful stay!\"")
            return
        elif to_go == "what is this" or to_go == "what is this?":
            print("\"This is the Automated People Mover, or \'APM\' for short. "
                  "Our APM service provides base workers with a convenient, safe way to travel between domes.\"")
        else:
            print("\n\"'" + user_input + "' not a valid response.\"")


