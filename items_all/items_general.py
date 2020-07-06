"""
Holds items that are used more than once, or are formatted to be used 
in a general sense
"""

from items import Item

class Clock(Item):
    def __init__(self, time_location="Minneapolis"):
        self.time_location = time_location
        super().__init__(name=[time_location + " Clock"], can_pick_up=True,
                         description="A traditional-looking clock set to " + self.time_location + " local time.")

class Drink(Item):
    def __init__(self, name, description, drink_response="*gulp*"):
        self.drink_response = drink_response
        super().__init__(name=name, description=description, can_pick_up=True)

    def drink(self):
        print(self.drink_response)

# TODO: MAYBE MAKE IT SO THAT IF YOU DRINK TOO MANY SOMETHING HAPPENS TO YOU TO MAKE YOU "DRUNK" IN GAME ===============================
class Booze(Drink):
    def __init__(self, name=["Booze"], description="A handle of 80-proof "
        "Henny", drink_response="Doesn't taste as good as it did "
        "back in college."):
        super().__init__(name=name,description=description,
            drink_response=drink_response)

class Mirror(Item):
    def __init__(self):
        super().__init__(name=["Mirror"],
                         description="There is an ugly person staring back at you.",
                         can_pick_up=False)

    def interact(self, player):
        print("There is an ugly person staring back at you.")

class Computer(Item):
    def __init__(self):
        super().__init__(name=["Computer"], can_pick_up=False,
                         description="A white, touch-screen monitor attached to the wall by a rotating beam. "
                                     "It's about a half-meter wide and a centimeter deep. It's turned on.")

    def interact(self, player):
        print("You pull up a chair and begin working at the computer...")
        scenarios.computer_usage(player)

class Bench(Item):
    def __init__(self, description="A long bench, wide enough to fit around four people."):
        super().__init__(name=["Bench"], can_pick_up=False,
                         description=description)

    def interact(self, player):
        print("It's not too comfy. Better than standing, though.")

class Photo(Item):
    def __init__(self, description="A photo"):
        super().__init__(name=["Photo", "Framed Photo"], 
            can_pick_up=True, description=description)

class Bowl(Item):
    def __init__(self, description="A small bowl"):
        super().__init__(name=["Bowl"], can_pick_up=False,
                         description=description)
class Desk(Item):
    def __init__(self, description= "A small desk"):
        super().__init__(name=["Desk"], can_pick_up=False,
                         description=description)
class Table(Item):
    def __init__(self, description="A large table with a polished finish.",
        name=["Table"]):
        super().__init__(name=name, can_pick_up=False, description=description)

class Toilet(Item):
    def __init__(self):
        super().__init__(name=["Toilet"], can_pick_up=False,
                         description="A standard, stainless-steel Toilet.")

    def interact(self, player):
        print("You've needed to take a crap since arriving. You now feel relieved.")

class Sink(Item):
    def __init__(self):
        super().__init__(name=["Sink"], can_pick_up=False,
                         description="A standard, stainless-steel sink.")

    def interact(self, player):
        print("You turn the sink on and wash your hands.")

class Food(Item):
    def __init__(self, name=["Food"], description="Some food...", eat_response="Tastes like chicken"):
        self.eat_response = eat_response
        super().__init__(name=name, description=description, can_pick_up=True)

    def eat(self):
        """
        Only prints the appropriate response (deletion of item is done in actions.py)
        """
        print(self.eat_response)

class Clothing(Item):
    def __init__(self, name=["CLOTHING"], description="CLOTHES DESCRIPTION"):
        super().__init__(name=name, can_pick_up=True, description=description)

class Couch(Item):
    def __init__(self):
        super().__init__(name=["Couch"], can_pick_up=False,
                         description="A sleek, black leather couch.")

    def interact(self, player):
        print("Huh, pretty comfy.")

class Bookshelf(Item):
    def __init__(self, description="DESCRIPTION HERE"):
        super().__init__(name=["Bookshelf"], can_pick_up=False,
            description=description)

class Book(Item):
    # Should always be overridden (obviously lol)
    def __init__(self, name=["BOOK"], description="BOOK DESCRIPTION"):
        super().__init__(name=name, description=description, can_pick_up=True)


class Chair(Item):
    def __init__(self, description="A standard, wooden chair."):
        super().__init__(name=["Chair", "Seat"], can_pick_up=False,
                         description=description)

    def interact(self, player):
        print("Surprisingly comfy.")


class Tablet(Item):
    def __init__(self):
        super().__init__(name=["Tablet"], can_pick_up=False,
            description="A touch-screen pad, held at shoulder-height by a "
            "narrow, cylindrical stand. The screen reads: \"Please swipe "
            "key card to begin\".")

class Tool(Item):
    def __init__(self, name, description, can_pick_up=True):
        super().__init__(name=name, description=description, can_pick_up=can_pick_up)

    def use(self, item, player):
        # Hammer destroying TCR Lock then updating description
        if "hammer" in [name.lower() for name in self.name] and "tcr lock" in [name.lower() for name in item.name]:
            print("After a few blows, you are able to shatter the mechanical lock.")
            for i, item in enumerate(world.tile_exists(player.location_x, player.location_y).items):
                if "tcr lock" in [name.lower() for name in item.name]:
                    del world.tile_exists(player.location_x, player.location_y).items[i]  # Destroying lock
                    world.tile_exists(player.location_x, player.location_y).description = \
                        "A medium-sized room with a track in the center surrounded by benches. "\
                        "A tablet rests on a stand at the end of the track. A horrible smell is coming "\
                        "from the Terra Communications Room."
                    for location, tile in world._world.items():
                        if world.tile_exists(location[0], location[1]):
                            if tile.name == "Terra Communications Room":
                                tile.can_enter = True
                                break
                    break
        # Hammer destroying Bar's Lock then updating description
        elif "hammer" in [name.lower() for name in self.name] and "bar lock" in [name.lower() for name in item.name]:
            print("With one strong strike you are able to shatter the lock. Opening the cabinet you are greeted by "
                  "a plethora of booze.")
            for i, item in enumerate(world.tile_exists(player.location_x, player.location_y).items):
                if "bar lock" in [name.lower() for name in item.name]:
                    del world.tile_exists(player.location_x, player.location_y).items[i]  # Destroying lock
                    for item in world.tile_exists(player.location_x, player.location_y).items:
                        if "cabinet" in [item_name.lower() for item_name in item.name]:
                            item.description = "A cabinet behind the bar. You've busted the lock on " \
                                               "it, exposing a variety of booze."
                            world.tile_exists(player.location_x, player.location_y).\
                                items += [Booze(), Booze(), Booze()]  #TODO: POSSIBLY CHANGE THIS SO THERE'S DIFFERENT KINDS? =======================================
                            break
                    break
        # Attempting to destroy jewelry counter glass with hammer
        elif "hammer" in [name.lower() for name in self.name] and "jewelry counter" in [name.lower() for name in item.name]:
            print("After a few blows it's clear this glass is too hard to be broken. Must be plexiglass.")
        # Attempting to destroy jewelry counter glass with hammer
        elif "hammer" in [name.lower() for name in self.name] and "jewelry lock" in [name.lower() for name in item.name]:
            print("No luck, the lock holds strong.")
        # Screwdriver removing jewelry counter screws then updating description
        elif "screwdriver" in [name.lower() for name in self.name] and "screw" in [name.lower() for name in item.name]:
            print("Using the screwdriver, you're able to take the screws off, exposing the jewelry inside.")
            for i, item in enumerate(world.tile_exists(player.location_x, player.location_y).items):
                if "screw" in [name.lower() for name in item.name]:
                    del world.tile_exists(player.location_x, player.location_y).items[i]  # Destroying screw
                    for item in world.tile_exists(player.location_x, player.location_y).items:
                        if "jewelry counter" in [item_name.lower() for item_name in item.name]:
                            item.description = "A very thick, glass case holding a variety of expensive items. "\
                                     "Its screws have been removed, exposing " \
                                     "a silver Rolex, a ring with a large, blue-ish stone, a gold necklace, " \
                                     "and more."
                            world.tile_exists(player.location_x, player.location_y).items += [
                                Jewelry(name=["Silver Rolex", "Rolex"], description="A silver Rolex watch. It tells "
                                        "the time in UTC."),
                                Jewelry(name=["Ring"], description="It's a bronze ring with a huge blue stone in "
                                        "the center. It almost looks like sapphire but has a hint of green as well."),
                                Jewelry(name=["Gold Necklace", "Necklace"], description="A gold, low-hanging "
                                        "necklace. Looks like something a rapper would wear to a club.")]
                            break
                    break
        else:
            print("Nothing happens")


class Shelf(Item):
    def __init__(self, description=""):
        super().__init__(name=["Shelf"], can_pick_up=False, description=description)


class Glass(Item):
    def __init__(self, description="A small whiskey glass"):
        super().__init__(name=["Glass", "Cup"],
            can_pick_up=True, description=description)

class Sign(Item):
    def __init__(self, desciption="\"...\""):
        super().__init__(name=["Sign"], can_pick_up=False, description=desciption)

