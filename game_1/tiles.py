import items, npcs, actions, world  # Correct even though it's red...


class Location:
    """ Template for a location/room. All places must derive from this """
    def __init__(self, x, y, items, name):
        self.x = x  # X-Coordinate of the location (should never be directly seen by player)
        self.y = y  # Y-Coordinate of the location (should never be directly seen by player)
        self.items = items  # List of objects (items) at this location
        self.name = name

    def adjacent_moves(self):
        """ Returns all move actions viable at the location. Can be overwritten """
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves  # A list of movement action objects available to the players

    def available_actions(self):
        """ Returns all actions viable at the location. """
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.KillPlayer())  # Suicides the player
        # Returns a list of all actions available to do in the location.
        # Players can always have the movement options and view inventory options but this module can be
        # expanded in child classes
        return moves


class Room(Location):
    def __init__(self, name, x, y, items, description):
        self.description = description  # Description of the location
        super().__init__(x, y, items, name)


class StartRoom(Room):
    def __init__(self, x, y):
        super().__init__(name="Starting Room", x=x, y=y,
                         description="A cold, dark room, lit by a single lightbulb hanging from the ceiling.",
                         items=[])


class NorthRoom(Room):
    def __init__(self, x, y):
        self.enemy = npcs.DerangedScientist()  # This room starts with a deranged scientist inside
        self.description = "A massive room with yellow walls. There's a crazy person in it!"
        super().__init__(name="North Room", x=x, y=y,
                         items=["Test1", "Test2"],
                         description=self.description)

    def available_actions(self):
        """ If enemy is alive, can only attack or flee. If enemy is dead, room works like normal. """
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()  # Why not actions.ViewInventory() too?? this is what he did online...

    def check_enemy(self):
        if self.enemy.is_alive():
            self.description = "A massive room with yellow walls. There's a crazy person in it!"
        else:
            self.description = "A massive room with yellow walls. Good thing there's no enemy ;)"


class EastRoom(Room):
    def __init__(self, x, y):
        super().__init__(name="East Room", x=x, y=y,
                         description="A tiny room with a desk.",
                         items=["Test1", "Test2", "Test3"])


class SouthRoom(Room):
    def __init__(self, x, y):
        super().__init__(name="South Room", x=x, y=y,
                         description="A small-ish room with a TV playing 'bandersnatch'.",
                         items=["Test1", "Test2", "Test3", "Test4"])


class WestRoom(Room):
    def __init__(self, x, y):
        super().__init__(name="West Room", x=x, y=y,
                         description="A pitch black room. Loud rock music is the only thing you can hear.",
                         items=[items.Knife(), items.Antimatter()])


class Hall(Location):
    def __init__(self, name, x, y, items=[]):
        self.description = "A long hallway barely bright enough to see your hand in front of your face"
        super().__init__(x, y, items, name)


class NorthHall(Hall):
    def __init__(self, x, y):
        super().__init__(name="North Hall", x=x, y=y)


class EastHall(Hall):
    def __init__(self, x, y):
        super().__init__(name="East Hall", x=x, y=y)


class SouthHall(Hall):
    def __init__(self, x, y):
        super().__init__(name="South Hall", x=x, y=y)


class WestHall(Hall):
    def __init__(self, x, y):
        super().__init__(name="West Hall", x=x, y=y)


class WinRoom(Room):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, name="Final Room",
                         description="This is the final room! You won!",
                         items=[])

    def win_game(self, player):
        player.victory = True
