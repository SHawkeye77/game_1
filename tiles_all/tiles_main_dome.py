""" This module holds all the specific tile classes for tiles in the 'landing base' section """

from tiles import Location
import items


class ApmTerminalB(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="APM Terminal B",
                         connected=["HallA"],
                         description="The APM track runs the length of the West end of the room. There are benches and "
                                     "a waiting area to the East where a tablet sits.",
                         items=[items.Tablet(), items.Bench()])


class SpiritualCenter(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Spiritual Center",
                         connected=["HallB", "Booth1", "Booth2"],
                         description="The room is scattered wih cushions and chairs. In one corner a "
                                     "tiny fountain pools into a small pond. There's a bookshelf on one wall. "
                                     "Connected on the east of the room are two personal booths.",
                         items=[items.Chair(), items.Cushion(), items.SpiritualCenterFountain(),
                                items.SpiritualCenterPond(), items.SpiritualCenterBookshelf(),
                                items.Book(name=["The Bible", "Bible"],
                                           description="1:1 In the beginning God created the heaven and the earth.\n"
                                                       "1:2 And the earth was without form, and void; and darkness was "
                                                       "upon the face of the deep. And the Spirit of God moved upon..."
                                                       "\nYou get bored and stop reading."),
                                items.Book(name=["The Quran", "Quran"],
                                           description="1:1 In the name of Allah, the Entirely Merciful, the "
                                                       "Especially Merciful.\n1:2 [All] praise is [due] to Allah, "
                                                       "Lord of the worlds -\n1:3 The Entirely Merciful, the "
                                                       "Especially Merciful,\n1:4 Sovereign of the..."
                                                       "\nYou get bored and stop reading."),
                                items.Book(name=["Tao Te Ching"],
                                           description="1:1 The Tao that can be trodden is not the enduring and "
                                                       "unchanging Tao. The name that can be named is not the "
                                                       "enduring and unchanging name.\n1:2 [Conceived of as] having "
                                                       "no name, it is the Originator of heaven and earth; "
                                                       "[conceived of as] having a name, it is...\nYou get bored and "
                                                       "stop reading.")])


class Booth1(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Booth 1",
                         connected=["SpiritualCenter"],
                         description="A cramped, soundproof booth barely big enough to fit a small bench and a little "
                                     "leg-room. It's no larger than your bedroom closet back on Terra.",
                         items=items.Bench(description="A tiny wooden bench."))


class Booth2(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Booth 2",
                         connected=["SpiritualCenter"],
                         description="A cramped, soundproof booth barely big enough to fit a small bench and a little "
                                     "leg-room. It's no larger than your bedroom closet back on Terra.",
                         items=items.Bench(description="A tiny wooden bench."))


class Bathrooms(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Bathrooms",
                         connected=["HallC"],
                         description="A clean bathroom with a bright, white finish. There are five stalls "
                                     "and a hallway cutting through the center of the room. At the end is a single "
                                     "sink and full length mirror.",
                         items=[items.Mirror(), items.Sink(), items.Toilet()])


class Gym(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Gym",
                         connected=["HallC"],
                         description="A complete gym filled with benches, squat racks, free weights, treadmills, "
                                     "bikes, rowing machines, and more...",
                         items=[items.WorkoutBench(), items.SquatRack(), items.Weight(), items.Treadmill(),
                                items.Bike(), items.RowingMachine()])


class Cafeteria(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Cafeteria",
                         connected=["HallE"],
                         description="Scattered about the room are tables of a variety of shapes and sizes. "
                                     "On the far wall is a large cyan tile with a black handle. Beneath it are "
                                     "four levers labeled \"S\", \"B\", \"L\", and \"D\", accompanied by a red button "
                                     "with \"Menu\" written on it...",
                         items=[items.Table(), items.Chair(), items.Tile(), items.Handle(), items.LeverB(),
                                items.LeverD(), items.LeverL(), items.LeverS(), items.MenuButton()])


class Bar(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Bar",
                         connected=["HallF"],
                         description="A dimly lit room complete with a red velvet booths and an old "
                                     "Steinway piano. Speakers playing 1950s jazz hang from the ceiling "
                                     "above a black-and-white checkerboard dance floor. At the back is a bar with a "
                                     "long cabinet behind it. You half expect Frank Sinatra to walk in.",
                         items=[items.Chair(), items.DanceFloor(), items.Speaker(), items.Piano(), items.Booth(),
                                items.Bar(), items.BarLock(), items.Cabinet()])
                        #TODO: CABINET SHOULD MAYBE BE COVEED BY SOMETHING OTHER THAN A LOCK SO IT'S NOT REPETITIVE


class MovieTheater(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Movie Theater",
                         connected=["HallH"],
                         description="The east wall is completely taken up by a massive digital screen. Facing "
                                     "the screen are rows of seats, separated into two sections by a narrow aisle. "
                                     "At the back is a projector. A box sits beneath it.",
                         items=[items.Screen(), items.Projector(), items.Chair(description="A red-leather recliner."),
                                items.MovieDisk(name=["2001: A Space Odyssey"], description=""
                                    "Title: 2001: A Space Odyssey\n\tReleased: 4/3/1968\n\tDirector: Stanley Kubrick"),
                                items.MovieDisk(name=["Star Wars"], description=""
                                    "Title: Star Wars\n\tReleased: 5/25/1977\n\tDirector: George Lucas"),
                                items.MovieDisk(name=["Sitting in the Stars"], description=""
                                    "Title: Sitting in the Stars\n\tReleased: 1/7/2034\n\tDirector: Owen Murphy"),
                                items.MovieDisk(name=["Blade Runner"], description=""
                                    "Title: Blade Runner\n\tReleased: 6/25/1982\n\tDirector: Ridley Scott"),
                                items.MovieBox(description="A cardboard storage box with slots to hold movies. "
                                    "The slots are labeled:\n - 2001: A Space Odyssey\n - Star Wars\n - Sitting in "
                                    "the Stars\n - Blade Runner")])


class MaintenanceRoom(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Maintenance Room",
                         connected=["HallI"],
                         description="There's a wooden table near the entrance with a pair of computers on it. "
                                     "Maintenance supplies lie in shelves on the south and east sides of the room. "
                                     "There's a sign taped up on the back wall.",
                         items=[items.Table(), items.Computer(), items.Chair(), items.WelcomeSign(),
                                items.Tool(name=["Hammer"], description="A standard, metal hammer."),
                                items.Tool(name=["Hammer"], description="A standard, metal hammer."),
                                items.Tool(name=["Screwdriver"],
                                           description="A metal screwdriver with a shank around 5 inches long."),
                                items.Tool(name=["Screwdriver"],
                                           description="A metal screwdriver with a shank around 5 inches long."),
                                items.Tool(name=["Ladder"], description="A foldable ladder at least 6 feet in height.",
                                           can_pick_up=False),
                                items.Tool(name=["Wrench"], description="Your standard wrench. "
                                                                        "No bigger than your hand."),
                                items.Tool(name=["Wrench"], description="Your standard wrench. "
                                                                        "No bigger than your hand.")])


class TerranCommodityStore(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Terran Commodity Store",
                         connected=["ShoppingCenter"],
                         description="The store is divided into three sections: A jewelry counter with glass-"
                                     "enclosed trinkets, a well-stocked bookshelf labeled \"Terran Classics\", and "
                                     "a clothing rack with luxury apparel.",
                         items=[items.ClothingRack(), items.TcsBookshelf(), items.JewelryLock(), items.JewelryCounter(),
                                items.Screw(),
                                items.Book(name=["The Nicomachean Ethics"], description="Probably Aristotle's "
                                           "best work. It's a tricky read but deeply thought-provoking."),
                                items.Book(name=["1984"], description="A dystopian tale about freedom. "
                                           "Looks like this one's a first edition."),
                                items.Book(name=["War and Peace"], description="Just looking at the book makes "
                                           "you drowsy."),
                                items.Book(name=["Slaughterhouse-Five"], description="You remember reading this "
                                           "back in high school. Wonder when Terra will get a base on Tralfamadore."),
                                items.Clothing(name=["Louis Vuitton Polo", "Polo"], description="A magenta "
                                           "polo with \"LV\" embroidered across it repeatedly in a diagonal pattern. "
                                           "The price tag reads $920 USD."),
                                items.Clothing(name=["Gucci Jacket", "Jacket"], description="A mostly black bomber "
                                           "jacket with \"GUCCI\" printed on its sleeves. On the back is a tiger and "
                                           "the words \"L'Aveugle Par Amour\". The price tag reads $1,040 USD."),
                                items.Clothing(name=["Versace Track Pants", "Pants", "Track Pants"], description=
                                           "A pair of golden-silk track pants covered with a "
                                           "Baroque-style print. The price tag reads $880 USD.")])


#TODO: Maybe need more food variety in here?
class ShoppingCenter(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Shopping Center",
                         connected=["HallJ"],
                         description="It's one of the largest rooms at the base. The shelves contain everything from "
                                     "canned goods to space-travel staples like rice and beans. There's even a "
                                     "hand scanner connected to a drug dispenser at the back of the store. Four slabs "
                                     "surrounding a black tile guard the exit. At the south end is a door "
                                     "leading to the Terran Commodity Store.",
                         items=[items.Shelf(), items.PayStation(), items.HandScanner(), items.DrugDispenser(),
                                items.Food(name=["Rice"], description="A bag of rice", eat_response="*gulp*"),
                                items.Food(name=["Rice"], description="A bag of rice", eat_response="*gulp*"),
                                items.Food(name=["Rice"], description="A bag of rice", eat_response="*gulp*"),
                                items.Food(name=["Beans"], description="The more you eat, the more...",
                                           eat_response="*gulp*"),
                                items.Food(name=["Beans"], description="The more you eat, the more...",
                                           eat_response="*gulp*"),
                                items.Food(name=["Beans"], description="The more you eat, the more...",
                                           eat_response="*gulp*"),
                                items.Food(name=["Soup"], description="Campbell's chunky! yum!", eat_response="*gulp*"
                                           "\nCanned, room temperature soup from a can... my favorite..."),
                                items.Food(name=["Soup"], description="Campbell's chunky! yum!", eat_response="*gulp*"
                                           "\nCanned, room temperature soup from a can... my favorite..."),
                                items.Food(name=["Soup"], description="Campbell's chunky! yum!", eat_response="*gulp*"
                                           "\nCanned, room temperature soup from a can... my favorite...")
                                ])


class SecurityCenter(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Security Center",
                         connected=["HallA", "SecurityOffice"],
                         description="Below a flight of computer monitors displaying security feeds is an L-shaped "
                                     "table with chairs tucked beneath it.",
                         items=[items.Chair(), items.SecurityMonitor(),
                                items.Table(description="An large, L-shaped table.")])


#TODO: Add stuff to cabinet in here (could have to do with lore or could just be for fun/expansion)
class SecurityOffice(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Security Office",
                         connected=["SecurityCenter"],
                         description="There's a circular table occupying most of the room. In the southeast corner is "
                                     "a cramped cubicle with a cabinet and a small computer.",
                         items=[items.Table(description="A circular conference table."), items.Cubicle(),
                                items.Computer(), items.Paperwork(), items.FilingCabinet(), items.Chair()])


class StorageArea(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Storage Area",
                         connected=["HallD"],
                         description="You're in a closet-sized entrance blocked off from a large storage area by "
                                     "clear plexiglass. There's a red button on the wall. The storage area is filled "
                                     "floor to ceiling with sealed crates.",
                         items=[items.StorageAreaButton(), items.Plexiglass()])


class Lounge(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Lounge",
                         connected=["HallG"],
                         description="A cozy, airy room. The artificial bricks, laminate wood-look flooring, and "
                                     "electric fireplace are reminiscent of your family cabin back home. Scattered "
                                     "around the room are bean-bag chairs, recliners, and a couple of massage "
                                     "chairs. There's even a small oxygen bar in the corner.",
                         items=[items.Fireplace(), items.MassageChair(), items.Recliner(), items.OxygenBar(),
                                items.OxygenBarJar(), items.OxygenBarTube()])

class Reception(Location):  
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Reception",
            connected=["HallI", "MentalHealthRoom", "SurgeryRoom", "EmergencyRoom"],
            description="A cute lobby with chairs and a reception desk. Doors "
                "to the emergency room, surgery room, and mental health room "
                "are on each end of the room. Written on the ER door in "
                "large, black lettering is: 'QUARENTINE - DO NOT ENTER'",
            items=[items.Chair(), items.Desk(), items.Photo(), 
                items.Computer(), items.Bowl(), items.Mint(), items.Mint(),
                items.Mint(), items.Phone()])

class EmergencyRoom(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Emergency Room",
            connected=["Reception"],
            description="Tables are pushed to the side, making room for an open area where nearly 15 "
                "corpses are haphazardly scattered. Blood clings to the tiles and the wretched stench of decaying "
                "bodies punctuates the room.",
            items=[items.Corpse(), items.Table()])

class SurgeryRoom(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Surgery Room",
            connected=["Reception"], description=
                "A sterile, white room with a bank of lights attached to the ceiling. "
                "There's a surgical tray on top of a rolling table. "
                "A stainless-steel operating table sits in the center of the room. There's a "
                "sink in the corner.",
            items=[items.Sink(), items.Table(description="A stainless-steel table large enough to fit human body..."),
                items.Tray(), items.Tool(name=["Tweezers"],description="Silver tweezers"),
                items.Tool(name=["Scalpel"],description="A silver scalpel with "
                    " a blade around an inch and a half long."),
                items.Tool(name=["Bone Clamp","Clamp"],description="A surgical "
                    "bone clamp. Looks like a pair of scissors but with curved, blunt edges.")])

class MentalHealthRoom(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Mental Health Room",
            connected=["Reception"],
            description="A couch sits across from a robotic head mounted on the wall. "
                "The head is labeled \"ELIZA\".",
            items=[items.Couch(), items.ELIZA_Chatbot()])

class Courtyard(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Courtyard",
            connected=["HallM", "HallN", "HallO", "HallP"],
            description="A wide open circular space capped only by the transparent, domed ceiling "
                "far above. The ground is artificial turf and there's a large, stone fountain "
                "flowing in the center. Around the perimeter is a running track.",
            items=[items.CourtyardFountain(), items.Turf(), items.Track()])


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
                         connected=["HallA", "HallC", "HallM", "SpiritualCenter"],
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

