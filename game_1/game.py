"""
This module runs the actual game (contains the main game loop).

To play from terminal:
1) navigate to the top level game_1 directory
2) run the command: export PYTHONPATH=$PWD
3) run the command: python3 game_1/game.py
"""

import world
from player import Player
from resources.lore import *
import parser


def play():
    """ Main function that will run to play the game """

    # Setting up the world
    world.load_tiles()  # Loads in the world specified in resources/map.csv
    player = Player()  # Creating a player object
    print(INTRODUCTION_TEXT)

    # Loading first room and printing intro text to it
    room = world.tile_exists(player.location_x, player.location_y)
    print("Location: " + room.name)
    print(room.description)

    # Main game loop that runs while the player is alive and no victory has been achieved
    while player.is_alive() and not player.victory:
        # Prompting user for action and printing all available actions.
        action_input = input("\nWhat do you do? ")  # Gathering action
        parser.parse_args(action_input, player)

    # If game stops because of death or victory, print corresponding text
    if not player.is_alive():
        print(DEATH_TEXT)
    if player.victory:
        print(CONCLUSION_TEXT)


# Running play() if this file is called.
if __name__ == "__main__":
    play()
