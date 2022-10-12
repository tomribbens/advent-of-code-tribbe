import math

from aocd.models import Puzzle, User

def does_player_win(player, boss):
    p_hp, p_atk, p_armor = player
    b_hp, b_atk, b_armor = boss

    real_p_atk = max(1, p_atk - b_armor)
    real_b_atk = max(1, b_atk - p_armor)
    p_turns = math.ceil(b_hp / real_p_atk)
    b_turns = math.ceil(p_hp / real_b_atk)

    if p_turns <= b_turns:
        return True
    else:
        return False


def shop_generator():
    weapons = {
        "Dagger": {"cost": 8, "damage": 4, "armor": 0},
        "Shortsword": {"cost": 10, "damage": 5, "armor": 0},
        "Warhammer": {"cost": 25, "damage": 6, "armor": 0},
        "Longsword": {"cost": 40, "damage": 7, "armor": 0},
        "Greataxe": {"cost": 74, "damage": 8, "armor": 0},
    }
    armors = {
        "Leather": {"cost": 13, "damage": 0, "armor": 1},
        "Chainmail": {"cost": 31, "damage": 0, "armor": 2},
        "Splintmail": {"cost": 53, "damage": 0, "armor": 3},
        "Bandedmail": {"cost": 75, "damage": 0, "armor": 4},
        "Platemail": {"cost": 102, "damage": 0, "armor": 5},
        "Nothing": {"cost": 0, "damage": 0, "armor": 0},
    }
    rings = {
        "Damage +1": {"cost": 25, "damage": 1, "armor": 0},
        "Damage +2": {"cost": 50, "damage": 2, "armor": 0},
        "Damage +3": {"cost": 100, "damage": 3, "armor": 0},
        "Defense +1": {"cost": 20, "damage": 0, "armor": 1},
        "Defense +2": {"cost": 40, "damage": 0, "armor": 2},
        "Defense +3": {"cost": 80, "damage": 0, "armor": 3},
        "Nothing1": {"cost": 0, "damage": 0, "armor": 0},
        "Nothing2": {"cost": 0, "damage": 0, "armor": 0},
    }

    for weapon in weapons.values():
        for armor in armors.values():
            for r1_name, ring1 in rings.items():
                for r2_name, ring2 in rings.items():
                    if r1_name == r2_name:
                        continue

                    cost = weapon["cost"] + armor["cost"] + ring1["cost"] + ring2["cost"]
                    damage = weapon["damage"] + armor["damage"] + ring1["damage"] + ring2["damage"]
                    defense = weapon["armor"] + armor["armor"] + ring1["armor"] + ring2["armor"]

                    yield cost, damage, defense


def solve(data):
    lines = data.splitlines()
    boss = {}
    for line in lines:
        stat, value = line.split(': ')
        boss[stat] = int(value)
    boss_stats = (boss["Hit Points"], boss["Damage"], boss["Armor"])

    min_cost = min([stats[0] for stats in shop_generator()
                    if does_player_win((100, stats[1], stats[2]), boss_stats)])
    max_cost = max([stats[0] for stats in shop_generator()
                    if not does_player_win((100, stats[1], stats[2]), boss_stats)])

    return str(min_cost), str(max_cost)

if __name__ == "__main__":
    p = Puzzle(year=2015, day=21)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
