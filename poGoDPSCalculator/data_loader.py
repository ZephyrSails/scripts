from classes import Type, FastMove, ChargedMove


def load_fast_moves():
    fast_moves = {}

    with open('data/fast_moves.csv', 'r') as file:
        for line in file.readlines()[2:]:
            type, name, dps, power_pvp, energy_pvp, cast_time, turns, dpt, ept = line.split(
                '\t')
            print(name, dps, power_pvp)
            fast_moves[name] = FastMove(name, type, dmg, cd, energy)


if __name__ == "__main__":
    load_fast_moves()
