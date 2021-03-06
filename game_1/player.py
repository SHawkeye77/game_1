import items, world

import random

# Starting HP for a new player
STARTING_HP = 100

# List of starting items for the player
# SHOULD BE CHANGED BACK AFTER TESTING
STARTING_ITEMS = [items.Tool(name=["Hammer"], description="FOR TESTING"),
                  items.Tool(name=["Screwdriver"], description="FOR TESTING"),
                  items.APMPass()]


class Player:
    def __init__(self):
        self.inventory = STARTING_ITEMS  # List of objects of items in player inventory
        self.hp = STARTING_HP
        self.location_x, self.location_y = world.starting_position  # Player location
        self.victory = False  # True if player has won

    def is_alive(self):
        """ True if player is alive, false otherwise """
        if self.hp > 0:
            return True
        else:
            return False

    def do_action(self, action, **kwargs):
        """ Run when player is supposed to do an action """
        action_method = getattr(self, action.method.__name__)  # Returns the action method given as "action" arg.
        if action_method:
            action_method(**kwargs)  # If the action method was found, it is run.

    def move(self, x, y):
        """ The general movement module. Always called for ALL player movement. """
        self.location_x = x
        self.location_y = y

        if world.tile_exists(self.location_x, self.location_y).been_entered:
            print("Location: " + str(world.tile_exists(self.location_x, self.location_y).name))
        else:
            world.tile_exists(self.location_x, self.location_y).first_entrance()
            world.tile_exists(self.location_x, self.location_y).been_entered = True

    def attack(self, enemy):
        """ Attacks 'enemy' with the highest-damage weapon in player's inventory """
        best_weapon = None
        max_damage = 0

        # Finding best weapon in your inventory
        for item in self.inventory:
            if isinstance(item, items.Weapon):  # Returns true if the item is a child class of the Weapon class
                if item.damage >= max_damage:
                    max_damage = item.damage
                    best_weapon = item

        # Applying damage from best weapon in inventory
        if best_weapon:  # If you have a weapon
            damage = best_weapon.damage
            print("You use {} against {}!".format(best_weapon.name[0], enemy.name))
            x = random.randint(1, 101)  # 1-100 random number for combat mechanics
            if 0 < x <= 15:  # Critical hit
                print("Critical hit!")
                damage *= 2
            elif 15 < x <= 30: # Checks for a miss
                print("Missed!")
                damage = 0
            enemy.hp -= damage
            if not enemy.is_alive():
                print("You killed {}!".format(enemy.name))
            else:
                print("{} HP is {}.".format(enemy.name, enemy.hp))
        else:
            print("You have no weapon! Nothing happens...")

    def flee(self, tile):
        """ Can be done instead of attacking. Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    def mod_hp(self, amount):
        """ Adds (or subtracts, if negative), the "amount" given to player's hp """
        self.hp += amount
