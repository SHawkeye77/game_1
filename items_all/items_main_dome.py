"""
Holds items specifically made in the main dome
"""

from items import Item
from items_all.items_general import *

######################## Mental Health Room Items ############################
class ELIZA_Chatbot(Item):
    def __init__(self):
        super().__init__(name=["Eliza", "Head", "Robotic Head", "Therapist"],
            can_pick_up=False,
            description="It's a robotic head resting body-less on the wall. "
            "Every couple of seconds it says \n\"Hello, I am ELIZA, your base therapist. "
            "How can I help you today?\"\n Looks like it wants to interact with you...")
    def interact(self, player):
        scenarios.talk_to_eliza(player)

############################ Emergency Room Items ############################
class Corpse(Item):
    def __init__(self):
        super().__init__(name=["Corpse", "Corpses"], can_pick_up=False,
            description="Each are in different stages of decay, but all seem "
                "to have the same problem. Their skin has peeled away in some "
                "sections while other parts have a surplus. Most are wearing "
                "standard UNEEA uniforms. You start to gag and feel "
                "light-headed.")
    def interact(self, player):
        print("Any closer you'll throw up... No thanks!")

############################# Storage Area Items #############################
class StorageAreaButton(Item):
    def __init__(self):
        super().__init__(name=["Button", "Red Button"], can_pick_up=False,
                         description="A red button about as big as your fist. Says \"Robotic Assistance\" on it...")

    def interact(self, player):
        scenarios.storage_area_robot(player)


########################### Security Center Items ###########################
#TODO: Could be a clue here that corresponds to which rooms are being shown on the monitor? Really shouldn't just be a red herring...
class SecurityMonitor(Item):
    def __init__(self):
        super().__init__(name=["Monitor", "Monitors", "Security Monitor", "Security Monitors"], can_pick_up=False,
                         description="There's 3 security monitors showing a hallway, a lounge, and a small shop.")



########################### Security Office Items ###########################
# TODO: could have all markable (with a pen/pencil) items inherit from a class called "Markable" which has a method that updates their description if they're written on
class Paperwork(Item):
    def __init__(self):
        super().__init__(name=["Paperwork", "Unmarked Paperwork", "Paper", \
            "Papers"], can_pick_up=True, description="Boring paperwork "
            "detailing legal procedures for theft, assault, "
            "public disturbance, yada yada yada....")

class FilingCabinet(Item):
    def __init__(self):
        super().__init__(name=["Cabinet", "Filing Cabinet"], can_pick_up=False,
            description="Your typical office filing cabinet.")

    def interact(self, player):
        print("Opening it reveals some paperwork.")

class Cubicle(Item):
    def __init__(self):
        super().__init__(name=["Cubicle"], can_pick_up=False,
                         description="A small office cubicle with a computer and cabinet.")

######################## Terran Commodity Store Items ########################
class Screw(Item):
    def __init__(self):
        super().__init__(name=["Screw", "Screws"], description="A 3 or 4 inch screw.", can_pick_up=False)

    def interact(self, player):
        print("It's too tight to twist with your hand.")

class Jewelry(Item):
    def __init__(self, name=[""], description="", interact_message="Nothing happens"):
        self.interact_message = interact_message
        super().__init__(name=name, description=description)

    def interact(self, player):
        print(self.interact_message)

class JewelryCounter(Item):
    def __init__(self):
        super().__init__(name=["Jewelry Counter", "Counter", "Glass"], can_pick_up=False,
            description="A very thick, glass case holding a variety of expensive items. "
            "It's sealed shut by a handful of screws and a digital lock. Its contents include "
            "a silver Rolex, a ring with a large, blue-ish stone, a gold necklace, "
            "and more.")

class Plexiglass(Item):
    def __init__(self):
        super().__init__(name=["Plexiglass", "Glass"], can_pick_up=False,
                         description="Thick plexiglass. Looks too durable to break.")

class JewelryLock(Item):
    def __init__(self):
        super().__init__(name=["Lock", "Jewelry Lock"], can_pick_up=False,
                         description="A thick, digital lock. Looks much more secure than the one from the Terra "
                                     "Communications Room.")

class ClothingRack(Item):
    def __init__(self):
        super().__init__(name=["Clothing Rack", "Rack"], can_pick_up=False,
            description="A long, silver clothing rack holding expensive designer clothes. A Gucci "
                "jacket, Louis Vuitton polo, and a pair of Versace track pants, among "
                "others things, catch your eye.")

############################### Reception Items #############################
class Phone(Item):
    def __init__(self):
        super().__init__(name=["Phone"], can_pick_up=False,
                         description="A landline; it looks like a slab of "
                         "metal.")

    def interact(self, player):
        print("You pick up the phone only to hear the dial tone. Pressing "
            "buttons does nothing. Phone lines must have been disconnected...")

class Mint(Food):
    def __init__(self):
        super().__init__(name=["Mint", "Mints"],description="An individually "
            "wrapped mint.", eat_response="Your breath smells great now! +5"
            "confidence points!") 

################################# Bar Items #################################
class Cabinet(Item):
    def __init__(self):
        super().__init__(name=["Cabinet"], can_pick_up=False,
                         description="A long cabinet behind the bar. It's secured by a lock.")

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

class DanceFloor(Item):
    def __init__(self):
        super().__init__(name=["Dance Floor", "Floor"], can_pick_up=False,
                         description="A black-and-white checkerboard dance floor that takes up the center of the room.")

    def interact(self, player):
        print("Nodding your head to the smooth jazz playing overhead you hop on to the dance floor and bust out "
              "some moves. Your boy's still got it.")

class Booth(Item):
    def __init__(self):
        super().__init__(name=["Booth", "Booths"], can_pick_up=False,
                         description="A red velvet booth.")

    def interact(self, player):
        print("You take a seat then immediately get up. This is no time for rest!")

class Bar(Item):
    def __init__(self):
        super().__init__(name=["Bar"], can_pick_up=False,
                         description="A long, curved bar with a wooden finish.")

class BarLock(Item):
    def __init__(self):
        super().__init__(name=["Lock", "Bar Lock"], can_pick_up=False,
                         description="An old, bulky, mechanical lock.")



################################ Lounge Items ################################
class BeanBagChair(Item):
    def __init__(self):
        super().__init__(name=["Bean-Bag Chair", "Bean Bag Chair", "Bean Bag", "Beanbag", "Bean-Bag"],
                         can_pick_up=False, description="A green bean-bag chair.")

    def interact(self, player):
        print("You sit down and sink in. It's so comfy you could pass out right now...")

class MassageChair(Item):
    def __init__(self):
        super().__init__(name=["Massage Chair", "Massage-Chair"], can_pick_up=False,
                         description="A full body massage chair.")

    def interact(self, player):
        print("Looks crazy comfy, how is there no line? Oh wait, it's because the people at the base are most " 
              "likely all dead...")

class Recliner(Item):
    def __init__(self):
        super().__init__(name=["Recliner"], can_pick_up=False,
                         description="A brown-leather recliner.")

    def interact(self, player):
        print("Comfy but sticky... ew")

class OxygenBar(Item):
    def __init__(self):
        super().__init__(name=["Oxygen Bar", "Bar"], can_pick_up=False,
                         description="A wooden bar. There're jars embedded in the wooden counter. Attached to them "
                                     "are tubes.")

class OxygenBarJar(Item):
    def __init__(self):
        super().__init__(name=["Jar", "Jars"], can_pick_up=False,
                         description="Looks like a beaker straight out of a mad-scientist's "
                                     "laboratory. Nothing visible is inside it, but there's a faint, pink glow.")

class OxygenBarTube(Item):
    def __init__(self):
        super().__init__(name=["Tube", "Tubes"], can_pick_up=False,
                         description="A clear tube coming from the top of a jar.")

    def interact(self, player):
        print("You stick the end of the tube in your nose and take a deep breath in. On the exhale you relax. "
              "It's a relaxing peppermint flavor.")

class Fireplace(Item):
    def __init__(self):
        super().__init__(name=["Fireplace", "Electric Fireplace"], can_pick_up=False,
                         description="A long, curved electric fireplace that lines the entirety of the back wall.")

    def interact(self, player):
        print("You rub your hands together and face your palms towards the fireplace. The pleasant heat "
              "reminds you of simpler days.")

############################ Movie Theatre Items ############################
class Screen(Item):
    def __init__(self):
        super().__init__(name=["Screen", "Movie Screen"], can_pick_up=False,
                         description="A giant, white screen.")

class Projector(Item):
    def __init__(self, description="A cinematic projector resting on a tripod. It's made to "
        "look like an old-timey projector, complete with rotating film reels and a wooden "
        "finish. That being said, it looks like you can just insert a digital disk into "
        "a slot on its back to get it going..."):
        super().__init__(name=["Projector"], can_pick_up=False,
            description=description)

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


############################## Cafeteria Items ##############################
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


########################### Shopping Center Items ###########################
class Shelf(Item):
    def __init__(self):
        super().__init__(name=["Shelf", "Shelves"], can_pick_up=False,
                         description="Basic, metal shelves containing canned and packages goods "
                                     "including rice, beans, soup, and more")

class PayStation(Item):
    def __init__(self):
        super().__init__(name=["Pay Station", "Slab", "Slabs", "Tile"], can_pick_up=False,
                         description="Four silver slabs, no higher than waist height, surround a black, glowing "
                                     "square tile.")

    def interact(self, player):
        print("You stand in the center of the slabs. A familiar voice greets you from the intercom above...\n"
              "\"Greetings, Mr. Adams, I hope your shopping went well today...\n. . .\n"
              "Your account has now been automatically charged for all items on your person. Have a wonderful day!\"")

class HandScanner(Item):
    def __init__(self):
        super().__init__(name=["Hand Scanner", "Hand-Scanner", "Scanner"], can_pick_up=False,
                         description="Four silver slabs, no higher than waist height, surround a black, glowing "
                                     "square tile.")

    def interact(self, player):
        print("You place your hand in the hand-scanner. After a second of processing, a voice says:\n\"You have no "
              "pharmaceuticals available for pickup at this time. Please check your prescription notice for details.\"")

class DrugDispenser(Item):
    def __init__(self):
        super().__init__(name=["Drug Dispenser", "Dispenser"], can_pick_up=False,
                         description="A huge black box that organizes and dispenses drugs for the base")

    def interact(self, player):
        print("Looks like you need to interact with the hand scanner to gain access.")

########################### Maintenance Room Items ###########################
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

############################# Surgery Room Items #############################
class Tray(Item):
    def __init__(self):
        super().__init__(name=["Tray", "Surgical Tray"], can_pick_up=False,
            description="A silver surgical tray holding a variety of medical "
            "instruments including a scalpel, tweezers, and a bone clamp.")

########################### Spiritual Center Items ###########################
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


############################### Courtyard Items ##############################
class CourtyardFountain(Item):
    def __init__(self):
        super().__init__(name=["Fountain"], can_pick_up=False,
            description="The fountain is a map of the solar system. Water flows from a model of the Sun at "
            "the top down over all the planets before being reclaimed in a small "
            "pool at the bottom.")

class Track(Item):
    def __init__(self):
        super().__init__(name=["Track", "Running Track"], can_pick_up=False,
            description="A rubber track two lanes wide circles around the entire dome.")
    def interact(self, player):
        print("You stretch out the hammies and start jogging... Feels good to move "
            "the legs after such a long rocket ride.")


class Turf(Item):
    def __init__(self):
        super().__init__(name=["Turf", "Ground"], can_pick_up=False,
            description="It's a cheap way to remind you of the green grass back "
            "home, but it works.")
    def interact(self, player):
        print("You take a seat cross-legged on the ground and smile. It'd be fun "
            "to have a picnic out here when this is all over...")

############################### Gym Items ##############################
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




