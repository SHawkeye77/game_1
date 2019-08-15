""" Module for dealing with the world we created """
""" NOTE: It now deals in csv files for reading it. 
"""

_world = {}  # Dictionary that will map coordinate pair to a tile
START_ROOM_NAME = "MovieTheater"  #TODO: SHOULD BE SWITCHED BACK TO "LandingPad" AFTER TESTING
starting_position = (0, 0)  # (x,y) tuple that will be set to the coordinates of the starting room


def load_tiles():
    """ Parses a file that describes the world space into the _world dictionary

    fills the "_world" dictionary that will map tuples of (x,y) coordinates to objects of rooms

    """
    with open('resources/map.csv', 'r') as f:
        rows = f.readlines()  # Splits file into list of rows (which are strings)
        x_max = len(rows[0].split(','))  # Assumes all rows contain the same number of cells (separated by commas)
        for y_val in range(len(rows)):  # For each row...
            cols = rows[y_val].split(',')  # A list where each element is text for the cell.
            for x_val in range(x_max):  # For each column
                tile_name = cols[x_val].replace('\n', '')  # Name (string) of that tile
                if tile_name == START_ROOM_NAME:  # Setting starting location for the game
                    global starting_position  # Lets us access this var even tho it's out of our scope
                    starting_position = (x_val, y_val)

                # For each (x,y) pair, create key/value pair where key is the (x,y) representing the location, and the
                # value is the constructed object of the type specified by that space
                _world[(x_val, y_val)] = \
                    None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x=x_val, y=y_val)


def tile_exists(x, y):
    """ Returns the object at given (x,y) location. If object doesn't exist, returns None """
    return _world.get((x, y))
