""" This module holds all the specific tile classes for tiles in the 'landing base' section """

from tiles import Location
import items, scenarios


class ApmTerminalB(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="APM Terminal B",
                         connected=["HallA"],
                         description="The APM track runs the length of the West end of the room. There are benches and "
                                     "a waiting area to the East where a tablet sits.",
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
                                     "leg-room. It's no larger than your bedroom closet back on Terra.")


class Booth2(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Booth 2",
                         connected=["SpiritualCenter"],
                         description="A cramped, soundproof booth barely big enough to fit a small bench and a little "
                                     "leg-room. It's no larger than your bedroom closet back on Terra.")


class Bathrooms(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Bathrooms",
                         connected=["HallC"],
                         description="A clean bathroom with a bright white finish. There are five stalls "
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
                         description="Scattered about the room are tables of a variety of shapes and sizes. "
                                     "On the far wall is a large cyan tile with a black handle. Beneath it are"
                                     "four levers labeled 'B', 'L', 'D', and 'S'.")


class Bar(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Bar",
                         connected=["HallF"],
                         description="A dimly lit room complete with a bar, red velvet booths, and an old "
                                     "Steinway piano. Speakers hang from the ceiling above a black-and-white "
                                     "checkerboard dance floor. You half expect Frank Sinatra to walk in.")


class MovieTheater(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Movie Theater",
                         connected=["HallH"],
                         description="The east wall is completely taken up by a massive digital screen. Facing "
                                     "the screen are rows of seats, separated into two sections by a narrow aisle. "
                                     "At the back is a projector. Some discs lay neatly beneath it.")


class MaintenanceRoom(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Maintenance Room",
                         connected=["HallI"],
                         description="There's a wooden table near the entrance with a pair of computers on it. "
                                     "Maintenance supplies lie in an opened closet on the south and east sides of the "
                                     "room.")


class TerranCommodityStore(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Terran Commodity Store",
                         connected=["ShoppingCenter"],
                         description="The store is divided into three sections: A jewelry counter with glass-"
                                     "enclosed trinkets, a well-stocked bookshelf labeled \"Terran Classics\", and "
                                     "a clothing section with luxury apparel.")


class ShoppingCenter(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Shopping Center",
                         connected=["HallJ"],
                         description="It's one of the largest rooms at the base. The shelves contain everything from "
                                     "canned goods to space-travel staples like rice and beans. There's even a "
                                     "small section of drugs and pharmaceutical products at the back. A pay station "
                                     "guards the exit.")


class SecurityCenter(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Security Center",
                         connected=["HallA", "SecurityOffice"],
                         description="Below a flight of monitors displaying security feeds is an L-shaped table with "
                                     "chairs tucked beneath it.")


class SecurityOffice(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Security Office",
                         connected=["SecurityCenter"],
                         description="There's a circular table occupying most of the room. In the southeast corner is "
                                     "a small cubicle with a cabinet and small computer. ")


class StorageArea(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Storage Area",
                         connected=["HallD"],
                         description="You're in a closet-sized entrance blocked off from a large storace area by "
                                     "clear plexiglass. There's a red button on the wall. The storage area is filled "
                                     "floor to ceiling with sealed crates.")  # THE ROBOT COULD BE BROKEN IF I DON'T FEEL LIKE CODING IN THE STUFF OR IT COULD ONLY BE ABLE TO GRAB CERTAIN THINGS


class Lounge(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Lounge",
                         connected=["HallG"],
                         description="A cozy, airy room. The artificial bricks, laminate wood-look flooring, and "
                                     "electric fireplace are reminiscent of your family cabin back home. Scattered "
                                     "around the room are bean-bag chairs, recliners, and even a couple massage "
                                     "chairs. There's even a small oxygen bar in the corner.")


class Reception(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Reception",
                         connected=["HallI", "MentalHealthRoom", "SurgeryRoom", "EmergencyRoom"],
                         description="A cute lobby with chairs and a modest reception desk.")  # ADD A PHONE AND COMPUTER AND FRAMED PHOTO AND A BOWL OF MINTS ON THE DESK? ADD TO DESCRIPTION?


class EmergencyRoom(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Emergency Room",
                         connected=["Reception"],
                         description="Tables are pushed to the side, making room for an open area where corpses "
                                     "are now scattered. Blood clings to the tiles and the wretched stench of decaying "
                                     "bodies punctuates the room.")


class SurgeryRoom(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Surgery Room",
                         connected=["Reception"],
                         description="A sterile, white room with a bank of lights attached to the ceiling. "
                                     "There's a tray on top of a rolling table. A white cloth covers its contents. "
                                     "A stainless-steel operating table sits in the center of the room. There's a "
                                     "sink in the corner.")


class MentalHealthRoom(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="MentalHealthRoom",
                         connected=["Reception"],
                         description="A couch sits across from a robotic head mounted on the wall. The head is "
                                     "labeled \"ELIZA\"")


class Courtyard(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Courtyard",
                         connected=["HallM", "HallN", "HallO", "HallP"],
                         description="A wide open circular space capped only by the transparent, domed ceiling "
                                     "far above. The ground is artificial turf and there's a large, stone fountain "
                                     "flowing with water in the center.")


class HallA(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall A",
                         connected=["HallL", "HallB", "ApmTerminalB", "SecurityCenter"],
                         description="A white tube with wires and tubes running along the ceiling. On the wall, in "
                                     "large, black lettering it reads \"Hall A\". Automatic doors wait "
                                     "at both ends.")


class HallB(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall B",
                         connected=["HallA", "HallC", "HallM", "SpiritualCenter", ""],
                         description="A white tube with wires and tubes running along the ceiling. On the wall, in "
                                     "large, black lettering it reads \"Hall B\". Automatic doors wait "
                                     "at both ends.")


class HallC(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall C",
                         connected=["HallB", "HallD", "Bathrooms", "Gym"],
                         description="A white tube with wires and tubes running along the ceiling. On the wall, in "
                                     "large, black lettering it reads \"Hall C\". Automatic doors wait "
                                     "at both ends.")


class HallD(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall D",
                         connected=["HallC", "HallE", "StorageArea"],
                         description="A white tube with wires and tubes running along the ceiling. On the wall, in "
                                     "large, black lettering it reads \"Hall D\". Automatic doors wait "
                                     "at both ends.")


class HallE(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall E",
                         connected=["HallD", "HallF", "HallN", "Cafeteria"],
                         description="A white tube with wires and tubes running along the ceiling. On the wall, in "
                                     "large, black lettering it reads \"Hall E\". Automatic doors wait "
                                     "at both ends.")


class HallF(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall F",
                         connected=["HallE", "HallG", "Bar"],
                         description="A white tube with wires and tubes running along the ceiling. On the wall, in "
                                     "large, black lettering it reads \"Hall F\". Automatic doors wait "
                                     "at both ends.")


class HallG(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall G",
                         connected=["HallF", "HallH", "Lounge"],
                         description="A white tube with wires and tubes running along the ceiling. On the wall, in "
                                     "large, black lettering it reads \"Hall G\". Automatic doors wait "
                                     "at both ends.")


class HallH(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall H",
                         connected=["HallG", "HallI", "HallO", "MovieTheater"],
                         description="A white tube with wires and tubes running along the ceiling. On the wall, in "
                                     "large, black lettering it reads \"Hall H\". Automatic doors wait "
                                     "at both ends.")


class HallI(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall I",
                         connected=["HallH", "HallJ", "Reception", "MaintenanceRoom"],
                         description="A white tube with wires and tubes running along the ceiling. On the wall, in "
                                     "large, black lettering it reads \"Hall I\". Automatic doors wait "
                                     "at both ends.")


class HallJ(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall J",
                         connected=["HallI", "HallK", "ShoppingCenter"],
                         description="A white tube with wires and tubes running along the ceiling. On the wall, in "
                                     "large, black lettering it reads \"Hall J\". Automatic doors wait "
                                     "at both ends.")


class HallK(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall K",
                         connected=["HallJ", "HallL", "HallP"],
                         description="A white tube with wires and tubes running along the ceiling. On the wall, in "
                                     "large, black lettering it reads \"Hall K\". Automatic doors wait "
                                     "at both ends.")


class HallL(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall L",
                         connected=["HallA", "HallK"],
                         description="A white tube with wires and tubes running along the ceiling. On the wall, in "
                                     "large, black lettering it reads \"Hall L\". Automatic doors wait "
                                     "at both ends.")


class HallM(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall M",
                         connected=["HallB", "Courtyard"],
                         description="A white tube with wires and tubes running along the ceiling. On the wall, in "
                                     "large, black lettering it reads \"Hall M\". Automatic doors wait "
                                     "at both ends.")


class HallN(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall N",
                         connected=["HallE", "Courtyard"],
                         description="A white tube with wires and tubes running along the ceiling. On the wall, in "
                                     "large, black lettering it reads \"Hall N\". Automatic doors wait "
                                     "at both ends.")


class HallO(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall O",
                         connected=["HallH", "Courtyard"],
                         description="A white tube with wires and tubes running along the ceiling. On the wall, in "
                                     "large, black lettering it reads \"Hall O\". Automatic doors wait "
                                     "at both ends.")


class HallP(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Hall P",
                         connected=["HallK", "Courtyard"],
                         description="A white tube with wires and tubes running along the ceiling. On the wall, in "
                                     "large, black lettering it reads \"Hall P\". Automatic doors wait "
                                     "at both ends.")

