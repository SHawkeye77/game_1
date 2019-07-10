import items, world

import random

STARTING_HP = 100  # Starting HP for a new player
STARTING_ITEMS = []  # List of starting items for the player


class Player:
    def __init__(self):
        self.inventory = STARTING_ITEMS
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

    def print_inventory(self):
        """ Prints all items in player's inventory """
        for item in self.inventory:
            print(item, end='\n')

    def move(self, dx, dy):
        """ The general movement module """
        self.location_x += dx
        self.location_y += dy
        # Printing the new location's name and description when you enter it
        print(world.tile_exists(self.location_x, self.location_y).name +
              '\n' + world.tile_exists(self.location_x, self.location_y).description)

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

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
        if best_weapon:
            damage = best_weapon.damage

        # Applying damage from best weapon in inventory
        if best_weapon:  # If you have a weapon
            print("You use {} against {}!".format(best_weapon.name, enemy.name))
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
