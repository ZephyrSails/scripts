from classes import *


if __name__ == "__main__":
    razorLeaf = FastMove("Razor Leaf", Type.Grass, 13, 1, 7)
    bulletSeed = FastMove("Bullet Seed", Type.Grass, 7, 1.1, 14)

    petalBlizzard = ChargedMove("Petal Blizzard", Type.Grass, 110, 2.6, 100)
    SludgeBomb = ChargedMove("Sludge Bomb", Type.Poison, 80, 2.3, 50)
    SolarBeam = ChargedMove("Solar Beam", Type.Grass, 180, 4.9, 100)

    mons = []
    for fast_move in [razorLeaf, bulletSeed]:
        for charged_move in [petalBlizzard, SludgeBomb, SolarBeam]:
            mons.append(Pokemon("Sunflora", [Type.Grass], fast_move, charged_move))

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
            mons.append(Pokemon("Mewtwo", [Type.Psychic], fast_move, charged_move))

    mons.sort(key=lambda mon: mon.cycle_dps())
    for mon in mons:
        mon.print_mon_cycle_dps()
