"""
This module holds all tiles classes (rooms, hallways, etc)
"""

import items, npcs, actions, world
import scenarios


class Location:
    """ Template for a single location/tile. All places must derive from this """
    def __init__(self, x, y, name, description, items=[], can_enter=True, been_entered=False, connected=[]):
        self.x = x  # X-Coordinate of the location (should never be directly seen by player)
        self.y = y  # Y-Coordinate of the location (should never be directly seen by player)
        self.items = items  # List of objects (items) at this location
        self.name = name
        self.description = description  # Description of the location
        self.can_enter = can_enter  # True if its enter-able, false if locked (or otherwise not enter-able)
        self.been_entered = been_entered  # False if room has never been entered by the player
        self.connected = connected  # List of strings corresponding to all names of connected
                                    # locations (in appropriate class format)

    def first_entrance(self):
        """ Is run only if it's the user's first time entering this location """
        print("Location: " + self.name + "\n" + self.description)


# ==================================================================================================================
# Creation of rooms for the landing base (doesn't include the outdoors stuff from the base).
# ==================================================================================================================


class LandingPad(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Landing Pad",
                         connected=["DetoxChamber"],
                         description="An outdoor landing pad with barely enough space for a ship to land. "
                                     "It's a tall, cylindrical room with a top open to the surrounding"
                                     " Martian environment. Blinking lights mark the way to the base's entrance.",
                         been_entered=True,
                         can_enter=False)


class DetoxChamber(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Detox Chamber",
                         connected=["LandingPad", "IntegrationRoom"],
                         description="A white, cylindrical room filled with vents and fans.")

    def first_entrance(self):
        print("Location: Detox Chamber\n")
        scenarios.detox_room_entrance()
        self.can_enter = False  # Making it so you can't go back in the detox chamber after leaving


class IntegrationRoom(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Integration Room",
                         connected=["DetoxChamber", "ApmTerminalA"],
                         items=[items.Plant(), items.Plant(), items.Couch(),
                                items.Table(description="A modest end table with an oak finish.")],
                         description="A simple room consisting of two couches. Each is accompanied by a table and "
                                     "potted plant.")

    def first_entrance(self):
        """ Is run only if it's the user's first time entering this location """
        for item in self.items:
            if issubclass(item.__class__, items.Drink):
                drink_name = item.name.lower()
                break

        print("Location: " + self.name)
        print("A simple room consisting of two couches. Each is accompanied by a potted plant and a table. "
              "On one sits a ", end="")
        if drink_name == "coffee" or drink_name == "tea":
            print("cup of " + drink_name + ".")
        elif drink_name == "water":
            print("glass of water.")
        elif drink_name == "coke":
            print("cold can of Coke.")
        else:
            print(drink_name)
            print("pile of dust.")


class ApmTerminalA(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="APM Terminal A",
                         description="A medium-sized room with a track in the center surrounded by benches. "
                                     "A tablet rests on a stand at the end of the track. A horrible smell is coming "
                                     "from the Terra Communications Room, which is locked by a large mechanical lock.",
                         connected=["IntegrationRoom", "Garage", "TerraCommunicationsRoom"],
                         items=[items.Bench(), items.Tablet(), items.Lock()])

    def first_entrance(self):
        """ Is run only if it's the user's first time entering this location """
        print("A medium-sized room with a track in the center surrounded by benches."
              "A tablet rests on a stand at the end of the track.\n "
              "A horrendous, rotten smell seems to be coming "
              "from the Terra Communications Room, which is, oddly, locked by a "
              "bulky, old-school mechanical lock...")


class Garage(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Garage",
                         description="A giant hangar covered by a transparent, domed roof. "
                                     "A closed garage door takes up all of the outside wall. "
                                     "On one end, a mechanical lever is attached to the wall. "
                                     "A few rovers are parked here. ",
                         connected=["ApmTerminalA", "GarageMaintenanceRoom"],
                         items=[items.Rover(), items.GarageLever()])


class TerraCommunicationsRoom(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Terra Communications Room",
                         description="Clocks labeled 'Sydney', 'New York', 'London', 'Dubai', and 'Pyongyang' "
                                     "are mounted on the wall. A long counter sprinkled with "
                                     "dials, buttons, and a computer stretches from wall to wall. "
                                     "In front of the computer sits the dead communications director.",
                         connected=["ApmTerminalA"],
                         items=[items.Table(), items.Chair(), items.Clock(time_location="Sydney"),
                                items.Clock(time_location="New York"), items.Clock(time_location="London"),
                                items.Clock(time_location="Dubai"), items.Clock(time_location="Pyongyang"),
                                items.DeadCommunicationsDirector(), items.Computer()],
                         can_enter=False)

    def first_entrance(self):
        print("Location: Terra Communications Room")
        print("Clocks labeled 'Sydney', 'New York', 'London', 'Dubai', and 'Pyongyang' are mounted on the wall. "
              "A long counter sprinkled with dials, buttons, and a computer stretches from wall to wall. "
              "In front of the computer sits who you assume is the communications "
              "director... dead. Something is horribly wrong with the corpse.")


class GarageMaintenanceRoom(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Garage Maintenance Room",
                         description="A small walk-in closet with a variety of maintenance supplies scattered about. "
                                     "A variety of tools: hammers, screwdrivers, wrenches, etc. sit "
                                     "beneath a wooden ladder.",
                         connected=["Garage"],
                         can_enter=True,
                         items=[items.Tool(name="Hammer", description="A standard, metal hammer."),
                                items.Tool(name="Screwdriver",
                                           description="A metal screwdriver with a shank around 5 inches long."),
                                items.Tool(name="Ladder", description="A foldable ladder at least 6 feet in height",
                                           can_pick_up=False),
                                items.Tool(name="Wrench", description="Your standard wrench. No bigger than your hand.")
                                ])

# ==================================================================================================================

