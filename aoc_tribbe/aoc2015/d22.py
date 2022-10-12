from itertools import product

from aocd.models import Puzzle


def do_fight(actions, boss, player=(50, 500), hard=False):
    b_hp, b_dmg = boss
    p_hp, p_mana = player
    p_armor = 0
    effects = {}

    def apply_effects():
        nonlocal p_armor, b_hp, p_mana, effects
        todelete = []
        for effect in effects:
            match effect:
                case "Shield":
                    p_armor += 7
                case "Poison":
                    b_hp -= 3
                case "Recharge":
                    p_mana += 101
            effects[effect] -= 1
            if effects[effect] == 0:
                todelete.append(effect)
        for effect in todelete:
            del effects[effect]

    for action in actions:
        p_armor = 0

        if hard:
            p_hp -= 1
            if p_hp <= 0:
                return "boss"

        apply_effects()
        match action:
            case "Magic Missile":
                if p_mana < 53:
                    return "Invalid"
                b_hp -= 4
                p_mana -= 53
            case "Drain":
                if p_mana < 73:
                    return "Invalid"
                b_hp -= 2
                p_hp += 2
                p_mana -= 73
            case "Shield":
                if "Shield" in effects or p_mana < 113:
                    return "Invalid"
                effects["Shield"] = 6
                p_mana -= 113
            case "Poison":
                if "Poison" in effects or p_mana < 173:
                    return "Invalid"
                effects["Poison"] = 6
                p_mana -= 173
            case "Recharge":
                if "Recharge" in effects or p_mana < 229:
                    return "Invalid"
                effects["Recharge"] = 5
                p_mana -= 229

        p_armor = 0
        apply_effects()

        if b_hp <= 0:
            return "player"

        p_hp -= max(1, b_dmg - p_armor)

        if p_hp <= 0:
            return "boss"


def spent_mana(actions):
    costs = {
        "Magic Missile": 53,
        "Drain": 73,
        "Shield": 113,
        "Poison": 173,
        "Recharge": 229,
    }
    total = sum([costs[action] for action in actions])
    return total


def generate_actions(boss, hard=False):
    possible_actions = ["Magic Missile", "Drain", "Shield", "Poison", "Recharge"]
    fights = [(spent_mana([action]), [action]) for action in possible_actions]
    min_cost = None
    winning_moves = None
    while fights:
        fight_cost, fight = fights.pop(0)
        if not min_cost or fight_cost < min_cost:
            winner = do_fight(fight, boss, hard=hard)
            if winner is None:
                for adding in possible_actions:
                    new_fight = fight + [adding]
                    new_fight_cost = spent_mana(new_fight)
                    if not min_cost or new_fight_cost < min_cost:
                        fights.append((new_fight_cost, new_fight))
            elif winner == "player":
                return fight_cost # Not sure the first result will always be the correct one. If not, remove this.
                min_cost = spent_mana(fight)
                winning_moves = fight

    return min_cost


def solve(data):
    lines = data.splitlines()
    boss = {}
    for line in lines:
        stat, val = line.split(': ')
        boss[stat] = int(val)

    boss_stats = (boss["Hit Points"], boss["Damage"])

    parta = generate_actions(boss_stats)
    partb = generate_actions(boss_stats, hard=True)

    return str(parta), str(partb)



if __name__ == "__main__":
    p = Puzzle(year=2015, day=22)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
