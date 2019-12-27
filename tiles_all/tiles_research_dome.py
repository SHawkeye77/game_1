""" 
This module holds all the specific tile classes for tiles in 
the 'research dome' section 
"""

from tiles import Location


class ApmTerminalC(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="APM Terminal C",
            connected=["MainHall"],
            description="ApmTerminalC DESCRIPTION HERE")

class ConferenceRoom(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Conference Room",
            connected=["OfficeHall"],
            description="CONFERANCEROOM DESCRIPTION HERE")

class Office1(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Office 1",
            connected=["OfficeHall"],
            description="Office1 DESCRIPTION HERE")

class Office2(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Office 2",
            connected=["OfficeHall"],
            description="Office2 DESCRIPTION HERE")

class Office3(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Office 3",
            connected=["OfficeHall"],
            description="Office3 DESCRIPTION HERE")

class OfficeHall(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Office Hall",
            connected=["Office1","Office2","Office3","ConferenceRoom","MainHall"],
            description="OfficeHall DESCRIPTION HERE")

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

class Lab1(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Lab 1",
            connected=["LabHall"],
            description="Lab1 DESCRIPTION HERE")

class Lab2(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Lab 2",
            connected=["LabHall"],
            description="Lab2 DESCRIPTION HERE")

class Lab3(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Lab 3",
            connected=["LabHall"],
            description="Lab3 DESCRIPTION HERE")

class ExtractContainmentArea(Location):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Extract Containment Area",
            connected=["LabHall"],
            description="ExtractContainmentArea DESCRIPTION HERE")
