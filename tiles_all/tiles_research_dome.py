""" 
This module holds all the specific tile classes for tiles in 
the 'research dome' section 
"""

from tiles import Location
import items


# ITEMS: ALREADY COMPLETED!
class ApmTerminalC(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="APM Terminal C",
            connected=["MainHall"],
            description="The APM enters this curved room from its western side. Just right of the track is a tablet "
                        "on a stand. Nearby are some benches.",
            items=[items.Tablet(), items.Bench()])

# ITEMS: Table, chairs, projector
class ConferenceRoom(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Conference Room",
            connected=["OfficeHall"],
            description="A large meeting room with a glass wall, exposing attendees to a beautiful view of the martian "
                "landscape outside. An ovoidal table sits at the center of the room surrounded by a handful of office "
                "chairs. A projector points to the eastern wall.")


# ITEMS: Computer, Desk, Chair, Bookshelf, Books, Armchair, Coffee Table, Czechoslovakian map, Framed Nobel Prize
class ZloOffice(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Zlo Office",
            connected=["OfficeHall"],
            description="A neat office with a sizable computer desk and office chair resting behind it. Mounted on the "
                        "wall is a map and framed award. On the other side of the room sits a bookshelf flanked by "
                        "two armchairs and a coffee table.")

# ITEMS: Cognac bottle, 2 Glasses, shelf, Scattered Papers, Computer, Desk, newton's cradle, espresso machine, Chair
class GomezOffice(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Gomez Office",
            connected=["OfficeHall"],
            description="A messy, cramped office with a computer desk and chair behind it. Resting on a shelf on the "
                        "far side is a bottle of cognac and two glasses.")
            # ON THE TABLE (IN IT'S DESCRIPTION): On the desk is a computer surrounded by a scattering of papers, a newton's cradle, and an espresso machine.


# ITEMS: PhD certificate, Drawer, Books/other stuff? (in drawers), Star Wars signed poster, Desk, family photo, Computer,
class AchebeOffice(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Achebe Office",
            connected=["OfficeHall"],
            description="A cramped but tidy office. A rolling chair sits behind a computer desk with drawers attached "
                        "to its sides. Hanging on the wall is a framed certificate as well as an old movie poster.")

class OfficeHall(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Office Hall",
            connected=["ZloOffice","GomezOffice","AchebeOffice","ConferenceRoom","MainHall"],
            description="It's essentially a large, white tube. There are doors to the offices and conference room "
                "here. A sign on the door to the southeastern office reads \"KNOCK BEFORE ENTERING\".")

class MainHall(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Main Hall",
            connected=["OfficeHall","ApmTerminalC","LabHall","DrillControlRoom"],
            description="MainHall DESCRIPTION HERE")

class DrillControlRoom(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Drill Control Room",
            connected=["MainHall"],
            description="DrillControlRoom DESCRIPTION HERE")

class LabHall(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Lab Hall",
            connected=["MainHall","Lab1","Lab2","Lab3","ExtractContainmentArea","LabBathroom"],
            description="LabHall DESCRIPTION HERE")

class LabBathroom(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Lab Bathroom",
            connected=["LabHall"],
            description="LabBathroom DESCRIPTION HERE")

class ZloLab(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Lab 1",
            connected=["LabHall"],
            description="Lab1 DESCRIPTION HERE")

class GomezLab(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Lab 2",
            connected=["LabHall"],
            description="Lab2 DESCRIPTION HERE")

class AchebeLab(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Lab 3",
            connected=["LabHall"],
            description="Lab3 DESCRIPTION HERE")

class ExtractContainmentArea(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Extract Containment Area",
            connected=["LabHall"],
            description="ExtractContainmentArea DESCRIPTION HERE")
