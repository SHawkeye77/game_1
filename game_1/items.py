"""
Items classes should always follow the format:
Capital letters for the start of new words.
Examples: Book, GarageDoor, ElectricalCable, etc.

NOTE: If an item description has multiple lines, each line after the first should start with a "\t" (tab)
NOTE: Items are interacted with by their associated item.name attribute. It should be intuitive to the player.
NOTE: Items must be able to accept player for all "use" overrides, and player for all "interact" overrides.
"""
import scenarios
import world


class Item:
    """ Base class for all items """
    def __init__(self, name, description, can_pick_up=True):
        self.name = name  # List of names for item (any of which can be used to reference it). First one should be main.
        self.description = description  # Description of item
        self.can_pick_up = can_pick_up  # Can the user add this to their inventory

    def use(self, item, player):
        """
        Used for "use _____ on _____" input
        Call when you want to use the current (self) item on the item that is passed in (in overridden methods of use).
        e.g. use key on door

        Args:
            item (object): other item we are going to use the current (self) item on.
            player (object): current user's player object
        Returns:
            N/A but uses self object on item object
        """
        # Override in child class if you want to have the object able to be used on something
        print("Nothing happens.")

    def interact(self, player):
        """
        Used for "interact with _____" input
        Call when you want to interact with the current (self) item
        e.g. interact with door
        """
        # Override in child class if you want to have the object interact-able
        print("Nothing happens.")


class DanceFloor(Item):
    def __init__(self):
        super().__init__(name=["Dance Floor", "Floor"], can_pick_up=False,
                         description="A black-and-white checkerboard dance floor that takes up the center of the room.")

    def interact(self, player):
        print("Nodding your head to the smooth jazz playing overhead you hop on to the dance floor and bust out "
              "some moves. Your boy's still got it.")


class Speaker(Item):
    def __init__(self):
        super().__init__(name=["Speaker", "Speakers"], can_pick_up=False,
                         description="A standard, black speaker.")

    def interact(self, player):
        print("You can't reach the speaker.")


class Piano(Item):
    def __init__(self):
        super().__init__(name=["Piano", "Steinway", "Steinway Piano"], can_pick_up=False,
                         description="Even though it's old the Steinway is in immaculate condition. "
                                     "It has a beautiful finish.")

    def interact(self, player):
        print("You were actually pretty good back in the day so you give it a shot.\n*Cracks Knuckles*\n"
              "Cringing at each missed note you quickly remember why you quit.")


class Bar(Item):
    def __init__(self):
        super().__init__(name=["Bar"], can_pick_up=False,
                         description="A long, curved bar with a wooden finish.")


class Booth(Item):
    def __init__(self):
        super().__init__(name=["Booth", "Booths"], can_pick_up=False,
                         description="A red velvet booth.")

    def interact(self, player):
        print("You take a seat then immediately get up. This is no time for rest!")


class TcrLock(Item):
    def __init__(self):
        super().__init__(name=["Lock", "TCR Lock"], can_pick_up=False,
                         description="An old, bulky, mechanical lock.")


class BarLock(Item):
    def __init__(self):
        super().__init__(name=["Lock", "Bar Lock"], can_pick_up=False,
                         description="An old, bulky, mechanical lock.")


class Cabinet(Item):
    def __init__(self):
        super().__init__(name=["Cabinet"], can_pick_up=False,
                         description="A long cabinet behind the bar. It's secured by a lock.")


class Couch(Item):
    def __init__(self):
        super().__init__(name=["Couch"], can_pick_up=False,
                         description="A sleek, black leather couch.")

    def interact(self, player):
        print("Huh, pretty comfy.")


class Tablet(Item):
    def __init__(self):
        super().__init__(name=["Tablet"], can_pick_up=False,
                         description="A touch-screen pad, held at shoulder-height by a narrow, cylindrical stand. "
                                     "The screen reads: \'Please swipe key card to begin\'")


class APMPass(Item):
    def __init__(self):
        super().__init__(name=["Key Card"],
                         description="It's dark-blue and looks like a credit-card.")

    def use(self, item, player):
        if "tablet" in [name.lower() for name in item.name]:
            print("*click*")
            print("From a speaker above, you're greeted by a familiar voice...")
            scenarios.apm_terminal(player)
        else:
            print("Nothing happens.")


class Note(Item):
    """ A slip of paper with info on it """
    def __init__(self, description):
        super().__init__(name=["Note"], description=description)


class Rover(Item):
    def __init__(self, locked=True, player_inside=False):
        self.locked = locked
        self.player_inside = player_inside  # True if the player is inside and piloting the rover
        super().__init__(name=["Rover"], can_pick_up=False,
                         description="A modest rover. The cabin is tube-shaped, and there's four huge wheels"
                                     " jutting out from each side.")

    def interact(self, player): # TO BE EXPANDED ON (OBVIOUSLY)
        if self.locked:
            print("It's locked. Looks like it requires a key-code to enter.")
        else:
            print("It's unlocked! You climb inside.")
            self.player_inside = True  # MAKE SURE WHEN YOU LEAVE ROVER THIS SWITCHES BACK TO FALSE!


class GarageLever(Item):
    # This lever controls opening/closing the garage bay door
    def __init__(self, garage_down=True):
        self.garage_down = garage_down
        super().__init__(name=["Lever"], can_pick_up=False,
                         description="A bulky mechanical lever. There's a wire attached to it that follows the "
                                     "dome above and ends at the garage door.")

    def interact(self, player):
        scenarios.opened_garage(player, self)


class Chair(Item):
    def __init__(self, description="A standard, wooden chair."):
        super().__init__(name=["Chair", "Seat"], can_pick_up=False,
                         description=description)

    def interact(self, player):
        print("Surprisingly comfy.")


class Screen(Item):
    def __init__(self):
        super().__init__(name=["Screen", "Movie Screen"], can_pick_up=False,
                         description="A giant, white screen.")


class Projector(Item):
    def __init__(self):
        super().__init__(name=["Projector"], can_pick_up=False,
                         description="A cinematic projector resting on a tripod. It's made to "
                                     "look like an old-timey projector, complete with rotating film reels and a wooden "
                                     "finish. That being said, it looks like you can just insert a digital disk into "
                                     "a slot on its back to get it going...")


class MovieBox(Item):
    def __init__(self, description="A cardboard box"):  # Description overridden to include what movies are in it
        super().__init__(name=["Box"], can_pick_up=False, description=description)


class MovieDisk(Item):
    """ A movie disk for use in the movie theater projector """
    def __init__(self, name=["MOVIE TITLE 1", "MOVIE TITLE ALTERNATIVE"], description="DESCRIPTION OF MOVIE"):
        super().__init__(name=name, can_pick_up=True, description=description)

    def use(self, item, player):
        if "2001: a space odyssey" in [name.lower() for name in self.name]:
            if "projector" in [name.lower() for name in item.name]:
                print("You pop in 2001 and the projector buzzes to life. You give it a shot but the movie is "
                      "pretty unbearable after the 10 minute monkey scene so you shut it off.")
            else:
                print("Nothing happens")
        elif "star wars" in [name.lower() for name in self.name]:
            if "projector" in [name.lower() for name in item.name]:
                print("You pop in Star Wars and the projector buzzes to life. You take a seat and admire it. So ahead "
                      "of its time.")
            else:
                print("Nothing happens")
        elif "blade runner" in [name.lower() for name in self.name]:
            if "projector" in [name.lower() for name in item.name]:
                print("You pop in Blade Runner and the projector buzzes to life. The worldbuilding in this movie is "
                      "almost unmatched. The set reminds you of modern day Hong Kong.")
            else:
                print("Nothing happens")
        elif "sitting in the stars" in [name.lower() for name in self.name]:  # This is a made-up movie lul
            if "projector" in [name.lower() for name in item.name]:
                print("You pop in Sitting in the Stars and the projector buzzes to life. It's pretty good for a "
                      "romantic-action-documentary-sci-fi-adventure-comedy-drama-horror flick.")
            else:
                print("Nothing happens")


class Tile(Item):
    def __init__(self):
        super().__init__(name=["Tile"], can_pick_up=False,
                         description="A round, cyan tile. It looks like it can be opened. On it is a handle.")


class Handle(Item):
    def __init__(self, interact_message="Pulling the handle opens the tile. Inside is a tray with nothing on it."):
        self.interact_message = interact_message
        super().__init__(name=["Handle"], can_pick_up=False,
                         description="A black handle.")

    def change_inside_tile(self, new_interact_message):
        self.interact_message = new_interact_message

    def interact(self, player):
        print(self.interact_message)


class MenuButton(Item):
    def __init__(self):
        super().__init__(name=["Button", "Menu"], can_pick_up=False,
                         description="A red button labeled \"Menu\"")

    def interact(self, player):
        print("A familiar voice greets you...\n"
              "\"Welcome to the UNEEA martian base cafeteria! Your menu for today is as follows:"
              "\n\tFor breakfast: scrambled eggs and fresh fruit!"
              "\n\tFor lunch: a scrumptious veggie and tofu wrap!"
              "\n\tFor dinner: mouth-watering lasagna!"
              "\n\tFor a snack: heart-healthy trail mix!"
              "\nEnjoy and have a wonderful day here at UNEEA's martian base!\"")


class WelcomeSign(Item):
    def __init__(self):
        super().__init__(name=["Sign"], can_pick_up=False,
                         description="It's a printed sign with a nice little welcome note:"
                                     "\n\"Welcome to the martian base, Mr. Adams, and congratulations on being a "
                                     "part of the biggest space-exploration mission in history! We hope that your "
                                     "stay as security manager is comfortable, useful, and, most importantly, "
                                     "enlightening. You can find your secure base login on the back of this poster.\" "
                                     "On the back of the poster it reads: \"u: MartianBaseUser143 "
                                     "p: !zz5v2562\"")


class LeverB(Item):
    def __init__(self):
        super().__init__(name=["Lever B", "B Lever", "B"], can_pick_up=False,
                         description="A silver lever labeled \"B\" in black lettering.")

    def interact(self, player):
        # Delete any other food in the room AND finding the Handle object
        for i, item in enumerate(world.tile_exists(player.location_x, player.location_y).items):
            if item.__class__.__name__ == "Handle":
                handle = item  # Should always hit this for one of the items
                continue
            if item.__class__.__name__ == "Food":
                del world.tile_exists(player.location_x, player.location_y).items[i]
                continue
        # Add the food item to the room
        world.tile_exists(player.location_x, player.location_y).items.append(Food(
            name=["Scrambled Egg Plate", "Eggs", "Breakfast", "Box"],
            description="A warm plate of scrambled eggs with a touch of salt and pepper. They're accompanied by a "
                        "bowl of fresh fruit."))
        # Changing the description of what's inside the tile
        handle.change_inside_tile("Pulling the handle opens the tile. Inside is a box labeled \"Breakfast\" containing "
                                  "some scrambled eggs and a bowl of fresh fruit.")
        # Hinting that something has changed
        print("After a few seconds, there's a slight rumbling from inside the tile followed by a *ding*")


class LeverD(Item):
    def __init__(self):
        super().__init__(name=["Lever D", "D Lever", "D"], can_pick_up=False,
                         description="A silver lever labeled \"D\" in black lettering.")

    def interact(self, player):
        # Delete any other food in the room AND finding the Handle object
        for i, item in enumerate(world.tile_exists(player.location_x, player.location_y).items):
            if item.__class__.__name__ == "Handle":
                handle = item  # Should always hit this for one of the items
                continue
            if item.__class__.__name__ == "Food":
                del world.tile_exists(player.location_x, player.location_y).items[i]
                continue
        # Add the food item to the room
        world.tile_exists(player.location_x, player.location_y).items.append(Food(
            name=["Lasagna", "Dinner", "Box"],
            description="A hot plate of Lasagna.",
            eat_response="gnam gnam!"))
        # Changing the description of what's inside the tile
        handle.change_inside_tile("Pulling the handle opens the tile. Inside is a box labeled \"Dinner\" containing "
                                  "a hot plate of lasagna.")
        # Hinting that something has changed
        print("After a few seconds, there's a slight rumbling from inside the tile followed by a *ding*")


class LeverL(Item):
    def __init__(self):
        super().__init__(name=["Lever L", "L Lever", "L"], can_pick_up=False,
                         description="A silver lever labeled \"L\" in black lettering.")

    def interact(self, player):
        # Delete any other food in the room AND finding the Handle object
        for i, item in enumerate(world.tile_exists(player.location_x, player.location_y).items):
            if item.__class__.__name__ == "Handle":
                handle = item  # Should always hit this for one of the items
                continue
            if item.__class__.__name__ == "Food":
                del world.tile_exists(player.location_x, player.location_y).items[i]
                continue
        # Add the food item to the room
        world.tile_exists(player.location_x, player.location_y).items.append(Food(
            name=["Wrap", "Lunch"],
            description="A chilled veggie and tofu wrap.",
            eat_response="mmmm healthy!"))
        # Changing the description of what's inside the tile
        handle.change_inside_tile("Pulling the handle opens the tile. Inside is a box labeled \"Lunch\" containing "
                                  "what looks like a veggie and tofu wrap.")
        # Hinting that something has changed
        print("After a few seconds, there's a slight rumbling from inside the tile followed by a *ding*")


class LeverS(Item):
    def __init__(self):
        super().__init__(name=["Lever S", "S Lever", "S"], can_pick_up=False,
                         description="A silver lever labeled \"S\" in black lettering.")

    def interact(self, player):
        # Delete any other food in the room AND finding the Handle object
        for i, item in enumerate(world.tile_exists(player.location_x, player.location_y).items):
            if item.__class__.__name__ == "Handle":
                handle = item  # Should always hit this for one of the items
                continue
            if item.__class__.__name__ == "Food":
                del world.tile_exists(player.location_x, player.location_y).items[i]
                continue
        # Add the food item to the room
        world.tile_exists(player.location_x, player.location_y).items.append(Food(
            name=["Trail Mix", "Snack", "Packet"],
            description="A small packet of nuts, chocolate, and dried fruit.",
            eat_response="*gulp*\nYum!"))
        # Changing the description of what's inside the tile
        handle.change_inside_tile("Pulling the handle opens the tile. Inside is a box labeled \"Snack\" containing "
                                  "a packet of trail mix.")
        # Hinting that something has changed
        print("After a few seconds, there's a slight rumbling from inside the tile followed by a *ding*")


class Food(Item):
    def __init__(self, name=["Food"], description="Some food...", eat_response="Tastes like chicken"):
        self.eat_response = eat_response
        super().__init__(name=name, description=description, can_pick_up=True)

    def eat(self):
        """
        Only prints the appropriate response (deletion of item is done in actions.py)
        """
        print(self.eat_response)


class Cushion(Item):
    def __init__(self):
        super().__init__(name=["Cushion"], can_pick_up=True,
                         description="A small cushion just large enough to sit cross-legged on.")

    def interact(self, player):
        print("You sit on it and smile, suddenly feeling more at ease.")


class SpiritualCenterFountain(Item):  #TODO: MAYBE IF YOU THROW A COIN IN SOMETHING HAPPENS??? ========================================
    def __init__(self):
        super().__init__(name=["Fountain"], can_pick_up=False,
                         description="Water flows from a high-up bowl, overflowing into larger bowls of increasing "
                                     "sizes below.")


class SpiritualCenterPond(Item):  #TODO: MAYBE IF YOU THROW A COIN IN SOMETHING HAPPENS??? ========================================
    def __init__(self):
        super().__init__(name=["Pond"], can_pick_up=False,
                         description="A clear pool of water. There's a drain at the bottom where the water is "
                                     "filtered.")


class SpiritualCenterBookshelf(Item):
    def __init__(self):
        super().__init__(name=["Bookshelf"], can_pick_up=False,
                         description="A dark, wooden bookshelf filled with religious texts.")  #TODO: MAYBE LIST SOME ACTUAL TEXTS? NEEDS TO BE UPDATED IF SOME ARE TAKEN THEN...


class Book(Item):
    def __init__(self, name=["BOOK"], description="BOOK DESCRIPTION"):
        super().__init__(name=name, description=description)


class Sink(Item):
    def __init__(self):
        super().__init__(name=["Sink"], can_pick_up=False,
                         description="A standard, stainless-steel sink.")

    def interact(self, player):
        print("You turn the sink on and wash your hands.")


class Toilet(Item):
    def __init__(self):
        super().__init__(name=["Toilet"], can_pick_up=False,
                         description="A standard, stainless-steel Toilet.")

    def interact(self, player):
        print("You've needed to take a crap since arriving. You now feel relieved.")


class WorkoutBench(Item):
    def __init__(self):
        super().__init__(name=["Bench", "Benches"], can_pick_up=False,
                         description="A red, padded workout bench that can be adjusted to different positions.")

    def interact(self, player):
        print("You rotate the back to a new position.")


class SquatRack(Item):
    def __init__(self):
        super().__init__(name=["Squat Rack"], can_pick_up=False,
                         description="A squat rack with a padded floor for olympic lifts.")

    def interact(self, player):
        print("You load up some weights and rip through a couple of sets. Your legs are sore now.")


class Weight(Item):
    def __init__(self):
        super().__init__(name=["Weight", "Weights", "Free Weights", "Free Weight", "Free Weights", "dumbbell",
                               "dumbbells"], can_pick_up=True, description="A 20 pound free weight")  #TODO: ADD DIFFERENT WEIGHTS SO THERE'S VARIATION AND MORE REALISM?

    def interact(self, player):
        print("You grind out some curls and examine your biceps. Not too shabby.")


class Treadmill(Item):
    def __init__(self):
        super().__init__(name=["Treadmill"], can_pick_up=False,
                         description="A dark-blue treadmill.")

    def interact(self, player):
        print("You adjust the dials and go for a quick jog. A few minutes later you end sweaty, huffing and puffing.")


class Bike(Item):
    def __init__(self):
        super().__init__(name=["Exercise Bike", "Bike"], can_pick_up=False,
                         description="A slick, silver stationary bike.")

    def interact(self, player):
        print("You take it for a quick spin. It doesn't feel great on your knees.")


class RowingMachine(Item):
    def __init__(self):
        super().__init__(name=["Rowing Machine"], can_pick_up=False,
                         description="It's filled with water used for the counterweight.")

    def interact(self, player):
        print("Now you're sweaty and your back is sore. Awesome.")


class Table(Item):
    def __init__(self, description="A large table with a polished finish."):
        super().__init__(name=["Table"], can_pick_up=False,
                         description=description)


class Clock(Item):
    def __init__(self, time_location="Minneapolis"):
        self.time_location = time_location
        super().__init__(name=[time_location + " Clock"], can_pick_up=True,
                         description="A traditional-looking clock set to " + self.time_location + " local time.")


class Transmitter(Item):
    def __init__(self):
        super().__init__(name=["Transmitter"], can_pick_up=False,
                         description="A metallic, tapering cylinder pointing up towards the sky. In the center you "
                                     "can see its photopropulsion apparatus. Looks like it's been tampered with...")


class DeadCommunicationsDirector(Item):
    def __init__(self):
        super().__init__(name=["Communications Director", "Corpse"], can_pick_up=False,
                         description="It is clear something awful happened to the director.\n"
                                     "His skin is, for the most part, torn. While some tears look like cuts, others "
                                     "are large enough to expose patches of his anatomy underneath... "
                                     "The intact portions of the man's skin are not normal either; at these spots "
                                     "the skin has clumped together and begun to sag from the man's body. "
                                     "There seems to be a note, as well as what looks like a small key card poking out "
                                     "of his breast pocket.")

    def interact(self, player):
        print("Yeah right, no way I'm touching that.")


class Computer(Item):
    def __init__(self):
        super().__init__(name=["Computer"], can_pick_up=False,
                         description="A white, touch-screen monitor attached to the wall by a rotating beam. "
                                     "It's about a meter wide and a centimeter deep. It's turned on.")

    def interact(self, player):
        print("You pull up a chair and begin working at the computer...")
        scenarios.computer_usage(player)


class Bench(Item):
    def __init__(self, description="A long bench, wide enough to fit around four people."):
        super().__init__(name=["Bench"], can_pick_up=False,
                         description=description)

    def interact(self, player):
        print("It's not too comfy. Better than standing, though.")


class Plant(Item):
    def __init__(self):
        super().__init__(name=["Plant", "Potted Plant"],
                         description="Looks like a Ficus Danielle, similar-looking to one at your apartment on Terra. "
                                     "It's clearly fake.")


class Drink(Item):
    def __init__(self, name, description, drink_response="*gulp*"):
        self.drink_response = drink_response
        super().__init__(name=name, description=description, can_pick_up=True)

    def drink(self):
        print(self.drink_response)


# TODO: MAYBE MAKE IT SO THAT IF YOU DRINK TOO MANY SOMETHING HAPPENS TO YOU TO MAKE YOU "DRUNK" IN GAME ===============================
class Booze(Drink):
    def __init__(self):
        super().__init__(name=["Booze"], description="A handle of 80-proof Henny",
                         drink_response="Doesn't taste as good as it did back in college.")


class Mirror(Item):
    def __init__(self):
        super().__init__(name=["Mirror"],
                         description="There is an ugly person staring back at you.",
                         can_pick_up=False)

    def interact(self, player):
        print("There is an ugly person staring back at you.")


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

        else:
            print("Nothing happens")
