""" 
This module holds all the specific tile classes for tiles in 
the 'research dome' section 
"""

from tiles import Location
import items

# TO ADD: Tablet, Bench
class ApmTerminalC(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="APM Terminal C",
            connected=["MainHall"],
            description="The APM enters this curved room from its western side. Just right of the track is a tablet "
                        "on a stand. Nearby are some benches.",
            items=[items.Tablet(), items.Bench()])

# TO ADD: Table, chairs, projector
class ConferenceRoom(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Conference Room",
            connected=["OfficeHall"],
            description="A large meeting room with a glass wall, exposing attendees to a beautiful view of the martian "
                "landscape outside. An ovoidal table sits at the center of the room surrounded by a handful of office "
                "chairs. A projector points to the eastern wall.")

class ZloOffice(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Zlo Office",
            connected=["OfficeHall"],
            description="ZloOffice DESCRIPTION HERE")

class GomezOffice(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Gomez Office",
            connected=["OfficeHall"],
            description="GomezOffice DESCRIPTION HERE")

class AchebeOffice(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Achebe Office",
            connected=["OfficeHall"],
            description="AchebeOffice DESCRIPTION HERE")

class OfficeHall(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Office Hall",
            connected=["ZloOffice","GomezOffice","AchebeOffice","ConferenceRoom","MainHall"],
            description="It's essentially a large, white tube. There are doors to the offices as well as the "
                "conference room here.")

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
