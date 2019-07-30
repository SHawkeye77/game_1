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
        self.name = name  # String name of the location (not list like items)
        self.description = description  # Description of the location
        self.can_enter = can_enter  # True if its enter-able, false if locked (or otherwise not enter-able)
        self.been_entered = been_entered  # False if room has never been entered by the player
        self.connected = connected  # List of strings corresponding to all names of connected
                                    # locations (in appropriate class-name (NOT class.name) format)

    def first_entrance(self):
        """ Is run only if it's the user's first time entering this location """
        print("Location: " + self.name + "\n" + self.description)


# ==================================================================================================================
# Creation of rooms for the landing dome (doesn't include the outdoors stuff from the base).
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
                drink_name = item.name[0].lower()
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
        print("A medium-sized room with a track in the center surrounded by benches. "
              "A tablet rests on a stand at the end of the track. "
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
                                     "dials, buttons, and a computer stretches from wall to wall. On the east side of "
                                     "the room sits the base's transmitter. "
                                     "In front of the computer sits the dead communications director.",
                         connected=["ApmTerminalA"],
                         can_enter=False,
                         items=[items.Table(), items.Chair(), items.Transmitter(), items.Clock(time_location="Sydney"),
                                items.Clock(time_location="New York"), items.Clock(time_location="London"),
                                items.Clock(time_location="Dubai"), items.Clock(time_location="Pyongyang"),
                                items.DeadCommunicationsDirector(), items.Computer(), items.APMPass(),
                                items.Note(description="A yellow post-it note with the following written on it:\n"
                                                       "\tu: luxxx825\n\tp: gellerfan334!")])

    def first_entrance(self):
        print("Location: Terra Communications Room")
        print("Clocks labeled 'Sydney', 'New York', 'London', 'Dubai', and 'Pyongyang' are mounted on the wall. "
              "A long counter sprinkled with dials, buttons, and a computer stretches from wall to wall. On the east "
              "side of the room sits the base's transmitter. "
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
                         items=[items.Tool(name=["Hammer"], description="A standard, metal hammer."),
                                items.Tool(name=["Screwdriver"],
                                           description="A metal screwdriver with a shank around 5 inches long."),
                                items.Tool(name=["Ladder"], description="A foldable ladder at least 6 feet in height.",
                                           can_pick_up=False),
                                items.Tool(name=["Wrench"], description="Your standard wrench. "
                                                                        "No bigger than your hand.")])

# ==================================================================================================================
# Creation of rooms for the main dome
# ==================================================================================================================


class ApmTerminalB(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="APM Terminal B",
                         connected=["HallA"],
                         description="APM TERMINAL B DESCRIPTION HERE")


class SpiritualCenter(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Spiritual Center",
                         connected=["HallB", "Booth1", "Booth2"],
                         description="SPIRITUAL CENTER DESCRIPTION HERE")


class Booth1(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Booth 1",
                         connected=["SpiritualCenter"],
                         description="BOOTH 1 DESCRIPTION HERE")


class Booth2(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Booth 2",
                         connected=["SpiritualCenter"],
                         description="BOOTH 2 DESCRIPTION HERE")


class Bathrooms(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Bathrooms",
                         connected=["HallC"],
                         description="BATHROOMS DESCRIPTION HERE")


class Gym(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Gym",
                         connected=["HallC"],
                         description="GYM DESCRIPTION HERE")


class Cafeteria(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Cafeteria",
                         connected=["HallE"],
                         description="GYM DESCRIPTION HERE")


class Bar(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Bar",
                         connected=["HallF"],
                         description="BAR DESCRIPTION HERE")


class MovieTheater(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Movie Theater",
                         connected=["HallH"],
                         description="MOVIE THEATER DESCRIPTION HERE")


class MaintenanceRoom(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Maintenance Room",
                         connected=["HallI"],
                         description="MAINTENANCE ROOM DESCRIPTION HERE")


class TerranCommodityStore(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Terran Commodity Store",
                         connected=["ShoppingCenter"],
                         description="TERRAN COMMODITY STORE DESCRIPTION HERE")


class ShoppingCenter(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Shopping Center",
                         connected=["HallJ"],
                         description="SHOPPING CENTER DESCRIPTION HERE")


class SecurityCenter(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Security Center",
                         connected=["HallA", "SecurityOffice"],
                         description="SECURITY CENTER DESCRIPTION HERE")


class SecurityOffice(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Security Office",
                         connected=["SecurityCenter"],
                         description="SECURITY OFFICE DESCRIPTION HERE")


class StorageArea(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Storage Area",
                         connected=["HallD"],
                         description="STORAGE AREA DESCRIPTION HERE")


class Lounge(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Lounge",
                         connected=["HallG"],
                         description="LOUNGE DESCRIPTION HERE")


class Reception(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Reception",
                         connected=["HallI", "MentalHealthRoom", "SurgeryRoom", "EmergencyRoom"],
                         description="RECEPTION DESCRIPTION HERE")


class EmergencyRoom(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Emergency Room",
                         connected=["Reception"],
                         description="EMERGENCY ROOM DESCRIPTION HERE")


class SurgeryRoom(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Surgery Room",
                         connected=["Reception"],
                         description="SURGERY ROOM DESCRIPTION HERE")


class MentalHealthRoom(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="MentalHealthRoom",
                         connected=["Reception"],
                         description="MENTAL HEALTH ROOM DESCRIPTION HERE")


class Courtyard(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Courtyard",
                         connected=["HallM", "HallN", "HallO", "HallP"],
                         description="COURTYARD DESCRIPTION HERE")


class HallA(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall A",
                         connected=["HallL", "HallB", "ApmTerminalB", "SecurityCenter"],
                         description="HALL A DESCRIPTION HERE")


class HallB(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall B",
                         connected=["HallA", "HallC", "HallM", "SpiritualCenter", ""],
                         description="HALL B DESCRIPTION HERE")


class HallC(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall C",
                         connected=["HallB", "HallD", "Bathrooms", "Gym"],
                         description="HALL C DESCRIPTION HERE")


class HallD(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall D",
                         connected=["HallC", "HallE", "StorageArea"],
                         description="HALL D DESCRIPTION HERE")


class HallE(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall E",
                         connected=["HallD", "HallF", "HallN", "Cafeteria"],
                         description="HALL E DESCRIPTION HERE")


class HallF(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall F",
                         connected=["HallE", "HallG", "Bar"],
                         description="HALL F DESCRIPTION HERE")


class HallG(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall G",
                         connected=["HallF", "HallH", "Lounge"],
                         description="HALL G DESCRIPTION HERE")


class HallH(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall H",
                         connected=["HallG", "HallI", "HallO", "MovieTheater"],
                         description="HALL H DESCRIPTION HERE")


class HallI(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall I",
                         connected=["HallH", "HallJ", "Reception", "MaintenanceRoom"],
                         description="HALL I DESCRIPTION HERE")


class HallJ(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall J",
                         connected=["HallI", "HallK", "ShoppingCenter"],
                         description="HALL J DESCRIPTION HERE")


class HallK(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall K",
                         connected=["HallJ", "HallL", "HallP"],
                         description="HALL K DESCRIPTION HERE")


class HallL(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall L",
                         connected=["HallA", "HallK"],
                         description="HALL L DESCRIPTION HERE")


class HallM(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall M",
                         connected=["HallB", "Courtyard"],
                         description="HALL M DESCRIPTION HERE")


class HallN(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall N",
                         connected=["HallE", "Courtyard"],
                         description="HALL N DESCRIPTION HERE")


class HallO(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall O",
                         connected=["HallH", "Courtyard"],
                         description="HALL O DESCRIPTION HERE")


class HallP(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall P",
                         connected=["HallK", "Courtyard"],
                         description="HALL P DESCRIPTION HERE")

