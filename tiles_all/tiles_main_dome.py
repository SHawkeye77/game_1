""" This module holds all the specific tile classes for tiles in the 'landing base' section """

from tiles import Location
import items, scenarios


class ApmTerminalB(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="APM Terminal B",
                         connected=["HallA"],
                         description="The APM track runs the length of the West end of the room. There's benches and a "
                                     "waiting area to the East where a tablet sits.",
                         items=[items.Tablet()])


class SpiritualCenter(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Spiritual Center",
                         connected=["HallB", "Booth1", "Booth2"],
                         description="The room is scattered wih cushions and chairs. In one corner a "
                                     "tiny fountain pools into a small pond. There's a bookshelf on one wall. "
                                     "Connected on the east of the room are two personal booths.")


class Booth1(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Booth 1",
                         connected=["SpiritualCenter"],
                         description="A cramped, soundproof booth barely big enough to fit a small bench and a little "
                                     "leg-room. It's no larger than your bedroom closet back on terra.")


class Booth2(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Booth 2",
                         connected=["SpiritualCenter"],
                         description="A cramped, soundproof booth barely big enough to fit a small bench and a little "
                                     "leg-room. It's no larger than your bedroom closet back on terra.")


class Bathrooms(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Bathrooms",
                         connected=["HallC"],
                         description="A clean bathroom with a bright white finish. There's five stalls "
                                     "and a hallway cutting through the center of the room. At the end is a single "
                                     "sink and full length mirror.",
                         items=[items.Mirror()])


class Gym(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Gym",
                         connected=["HallC"],
                         description="A complete gym filled with benches, squat racks, free weights, treadmills, "
                                     "bikes, rowing machines, and more...")


class Cafeteria(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Cafeteria",
                         connected=["HallE"],
                         description="CAFE DESCRIPTION HERE")


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

