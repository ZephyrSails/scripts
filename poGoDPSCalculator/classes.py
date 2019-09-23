from enum import Enum


class Type(Enum):
    Bug = 1
    Dark = 2
    Dragon = 3
    Electric = 4
    Fairy = 5
    Fighting = 6
    Fire = 7
    Flying = 8
    Ghost = 9
    Grass = 10
    Ground = 11
    Ice = 12
    Normal = 13
    Poison = 14
    Psychic = 15
    Rock = 16
    Steel = 17
    Water = 18


class Move:
    def __init__(self, name, type, dmg, cd, energy):
        self.name = name
        self.type = type
        self.dmg = dmg
        self.cd = cd
        self.energy = energy

    def dps(self, mon_types):
        return self.cycle_dmg(mon_types) / self.cd

    def cycle_dmg(self, mon_types):
        return self.dmg * (1.2 if (self.type in mon_types) else 1)


class FastMove(Move):
    pass


class ChargedMove(Move):
    pass


class Pokemon:
    def __init__(self, name, types, fast_move, charged_move):
        self.name = name
        self.types = types
        self.fast_move = fast_move
        self.charged_move = charged_move

    def cycle_dps(self):
        time = 0
        total_dmg = 0
        energy = 0
        while energy < self.charged_move.energy:
            time += self.fast_move.cd
            total_dmg += self.fast_move.cycle_dmg(self.types)
            energy += self.fast_move.energy

        time += self.charged_move.cd
        total_dmg += self.charged_move.cycle_dmg(self.types)
        return total_dmg / time

    def print_mon_cycle_dps(self):
        print("{} with {} and {} 's cycle dps is: {}".format(
            self.name, self.fast_move.name, self.charged_move.name,
            self.cycle_dps()))
