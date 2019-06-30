class NPC:
    """ Basic parent class for any non player controlled characters """
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        """ Returns if NPC is alive or not """
        if self.hp > 0:
            return True
        else:
            return False


class StarvingDog(NPC):
    def __init__(self):
        super().__init__(name="Starving Dog", hp=10, damage=2)


class DerangedScientist(NPC):
    def __init__(self):
        super().__init__(name="Deranged Scientist", hp=15, damage=2)

