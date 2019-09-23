from enum import Enum


class Type(Enum):
    Bug = 1
    Dark = 2
    Dragon = 3
    Electric = 4
    Fairy = 5
    Fight = 6
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


class PokeMon:
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


if __name__ == "__main__":
    razorLeaf = FastMove("Razor Leaf", Type.Grass, 13, 1, 7)
    bulletSeed = FastMove("Bullet Seed", Type.Grass, 7, 1.1, 14)

    petalBlizzard = ChargedMove("Petal Blizzard", Type.Grass, 110, 2.6, 100)
    SludgeBomb = ChargedMove("Sludge Bomb", Type.Poison, 80, 2.3, 50)
    SolarBeam = ChargedMove("Solar Beam", Type.Grass, 180, 4.9, 100)

    mons = []
    for fast_move in [razorLeaf, bulletSeed]:
        for charged_move in [petalBlizzard, SludgeBomb, SolarBeam]:
            mons.append(PokeMon("Sunflora", [Type.Grass], fast_move, charged_move))

    mons.sort(key=lambda mon: mon.cycle_dps())
    for mon in mons:
        mon.print_mon_cycle_dps()

    psychoCut = FastMove("Psycho Cut", Type.Psychic, 5, 0.6, 8)
    confusion = FastMove("Confusion", Type.Psychic, 20, 1.6, 15)

    physic = ChargedMove("Physic", Type.Psychic, 100, 2.8, 100)
    psystrike = ChargedMove("Psystrike", Type.Psychic, 90, 2.3, 50)

    mons = []
    for fast_move in [psychoCut, confusion]:
        for charged_move in [physic, psystrike]:
            mons.append(PokeMon("Mewtwo", [Type.Psychic], fast_move, charged_move))

    mons.sort(key=lambda mon: mon.cycle_dps())
    for mon in mons:
        mon.print_mon_cycle_dps()
