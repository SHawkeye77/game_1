""" 
This module holds all the specific tile classes for tiles in 
the 'research dome' section 
"""

from tiles import Location
import items as i


class ApmTerminalC(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="APM Terminal C",
            connected=["MainHall"],
            description="The APM enters this curved room from its western "
                "side. Just right of the track is a tablet on a stand. Nearby "
                "are some benches.",
            items=[i.Tablet(), i.Bench()])

class ConferenceRoom(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Conference Room",
            connected=["OfficeHall"],
            description="A large meeting room with a glass wall, exposing "
                "attendees to a beautiful view of the martian landscape "
                "outside. An ovoidal table sits at the center of the room "
                "surrounded by a handful of office chairs. A "
                "projector points to the eastern wall.",
            items=[i.Table(description="A long, ovoidal table. It has a "
                "gray finish"), i.Chair(description="A black swivel "
                "chair"), i.Projector(description="A sleek, white "
                "projector")])

# TODO: Modify russian nesting doll (in items.py) to add something at the center!!!!!!!!!!!!!!!!!!!!!!!!!
class ZloOffice(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Zlo Office",
            connected=["OfficeHall"],
            description="A neat office with a sizable computer desk and "
                "office chair resting behind it. Mounted on the "
                "wall is a map and framed award. On the other side of the "
                "room sits a bookshelf flanked by two armchairs and a "
                "coffee table. On it sits a Russian nesting doll.",
            items=[i.Computer(), i.Desk(description="A large computer desk."),
                i.Chair(description="A nice office chair"), i.ArmChair(),
                i.NobelPrize(), i.Map(), i.Table(name=["Table","Coffee Table"],
                description="A wooden coffee table. The surface sits "
                "at about knee height"), i.ZloBookshelf(),
                i.Book(name=["Ningen Shikkaku"], description="It's all in "
                "Japanese. Only thing you can decipher is the author's name: "
                "\"Osamu Dazai\""), i.Book(name=["The Jungle"],description=""
                "\"Chapter 1... It was four o'clock when the ceremony was "
                "over and the carriages began to arrive. There had been a "
                "crowd following all the way\" it continues... "
                "You think you may have read this back in high school."), 
                i.Book(name=["Povidky z pekla a jine", "Povidsky"], 
                description="Its all in some Eastern-European "
                "looking language. Author seems to be Marie Majerova."),
                i.RussianNestingDoll()])

class AchebeOffice(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Achebe Office",
            connected=["OfficeHall"],
            description="A cramped but tidy office. A rolling chair sits "
                "behind a computer desk with drawers attached "
                "to its sides. Hanging on the wall is a framed certificate "
                "as well as an old movie poster.",
            items=[i.Poster(), i.Altoids(), i.Altoids(), i.Altoids(),
                i.Computer(), i.AchebePhd(),i.Drawers(), i.Desk(description=\
                "A small office Desk. Neatly placed next to the computer sits "
                "a framed photo, a box of tissues, a pen, and a tin of "
                "Altoids."), i.Photo(description="A picture of three young "
                "women at a pier."), i.Pen(), i.PostItNotes(), i.WetWipes(),
                i.Book(name=["The Sirens of Titan"], description="\"Every "
                "one now knows how to find the meaning of life within "
                "himself. But mankind wasn't always so lucky. Less than a "
                "century ago men and women did not have easy access to "
                "the puzzle boxes within them...\" it continues on but "
                "you stop reading."), i.Chair(description="A standard "
                "rolling chair.")])

# 2 Glasses, shelf, Scattered Papers (with coffee stains on them), 
# Computer, Desk, newton's cradle, espresso machine, Chair, C.D Oro scarf
class GomezOffice(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Gomez Office",
            connected=["OfficeHall"],
            description="A messy, cramped office with a computer desk piled "
                "high with clutter. Resting on a shelf is a bottle and two "
                "glasses. Hanging up behind it is a scarf.",
            items=[i.Booze(name=["Bottle","Tequila"], description="About a "
                "liter of an oaky liquid. It's labeled \"Casamigos "
                "Reposado\".")])
    # ON THE TABLE (IN IT'S DESCRIPTION): On the desk is a computer surrounded 
    # by a scattering of papers, a newton's cradle, and an espresso machine.

# ITEMS: Sign (that says \"KNOCK BEFORE ENTERING\")
class OfficeHall(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Office Hall",
            connected=["ZloOffice","GomezOffice","AchebeOffice","ConferenceRoom","MainHall"],
            description="A white, cylindrical tube. There are doors to the offices and conference room. "
                        "A sign is tacked on to the door to the southeastern office.")

# ITEMS: ALREADY COMPLETED! (NONE)
class MainHall(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Main Hall",
            connected=["OfficeHall","ApmTerminalC","LabHall","DrillControlRoom"],
            description="A rectangular, white prism. To the east is the lab wing, and to the west is the offices.")

# ITEMS: Computers, Whiteboard (you can write on it), chairs, table, Holes and drill (for 'examine'ing)
# Note: If user tries to 'interact with drill' have it print "The drill looks to be electronically operated"
class DrillControlRoom(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Drill Control Room",
            connected=["MainHall"],
            description="A glass wall exposes the outside, where a metal arm connects to a massive drill. It looks "
                        "to have made hundreds of perforations into the Martian soil. Inside, chairs sit behind an "
                        "array of computers. On the western wall hangs a whiteboard.")

# ITEMS: Sign (that says \"KNOCK BEFORE ENTERING\") (for zlo's lab)
class LabHall(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Lab Hall",
            connected=["MainHall","Lab1","Lab2","Lab3","ExtractContainmentArea","LabBathroom"],
            description="A white, cylindrical tube. There are doors to the labs, bathroom, and extract containment "
                        "room. A sign is tacked on the door to the southwestern office.")

# ITEMS: ALREADY COMPLETED!
class LabBathroom(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Lab Bathroom",
            connected=["LabHall"],
            description="A single bathroom stall with a toilet, mirror, and sink.",
            items=[i.Mirror(), i.Sink(), i.Toilet()])

# ITEMS: table, stool, microscope, tank (holding microorganisms), beaker, strainer, Czech Republic (also Czechloslovakian) flag
class ZloLab(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Lab 1",
            connected=["LabHall"],
            description="There's one large, rectangular table at the center. On it sits a massive microscope, some beakers, and a strainer. "
                        "On the south end of the room is a container that looks like a fishtank, filled with two or three inches of "
                        "a viscous, gray liquid. A flag hangs on one end of the room.")

# ITEMS: Tables, stools, beakers, 3 bowls, 2 canisters of liquid (interactable?), sink, papers
class GomezLab(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Lab 2",
            connected=["LabHall"],
            description="The layout reminds you of a high school chemistry lab. There are two long tables and a couple of stools. On one table "
                        "there's lab supplies including beakers and a few large bowls. "
                        "Mounted on the wall are two large canisters filled with liquid." 
                        "On the other table there's a built-in sink, surrounded by a scattering of papers.")
        # one pitcher is really hot, one really cold (temperatures are regulated by tubes going into the wall)

# ITEMS: Tables, stools, beakers, gas stove, rock pick, containers, scale, posters (enterprise, millenium falcoln, YBN Lorkeer [made up])
class AchebeLab(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Lab 3",
            connected=["LabHall"],
            description="The layout reminds you of a high school chemistry lab. There are two long tables and a couple of stools. On a table "
                        "sits lab supplies including beakers, a rock pick, some containers, a scale, and "
                        "what looks like a gas stove. Some posters hang on the wall.")


# ITEMS: Tube, containment isolator, containers, shelves
class ExtractContainmentArea(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Extract Containment Area",
            connected=["LabHall"],
            description="The majority of the room is dozens of drawers on shelves. A tube, which looks "
                        "accessible by the main drill, connects the drilling area to "
                        "a large, transparent box, labeled \'Containment Isolator\'.")
        # "CONTAINMENT ISOLATOR" - A SEALED, TRANSPARENT BOX WITH GLOVES EMBEDDED IN IT SO YOU CAN MEDDLE WITH WHAT'S INSIDE WITHOUT INFECTING IT




