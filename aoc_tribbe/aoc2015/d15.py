import re
from collections import defaultdict

from aocd.models import Puzzle


def recipe_generator(n, total):
    if n == 1:
        yield [total]
    else:
        start = 0

        for i in range(start, total+1):
            left = total - i
            for y in recipe_generator(n-1, left):
                yield [i] + y

def get_cookie_scores(ingredients, ingredient_properties):
    scores = defaultdict(int)

    for ingredient, qty in ingredients.items():
        for prop, value in ingredient_properties[ingredient].items():
            scores[prop] += qty * value

    for prop, score in scores.items():
        if score < 0:
            scores[prop] = 0

    return scores


def get_combined_score(ingredients, ingredient_properties, target_calories=None):
    scores = get_cookie_scores(ingredients, ingredient_properties)
    if target_calories and scores["calories"] != target_calories:
        return 0
    return scores["capacity"] * scores["durability"] * scores["flavor"] * scores["texture"]


def solve(data):
    lines = data.splitlines()
    ingredient_properties = defaultdict(dict)
    pattern = re.compile(
        r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d), calories (-?\d+)')

    for line in lines:
        match = pattern.search(line)
        ingredient, capacity, durability, flavor, texture, calories = match.groups()
        ingredient_properties[ingredient] = {
            "capacity": int(capacity),
            "durability": int(durability),
            "flavor": int(flavor),
            "texture": int(texture),
            "calories": int(calories)
        }

    ingredients = list(ingredient_properties.keys())
    parta = max(
        [get_combined_score(recipe, ingredient_properties) for recipe in
            [dict(zip(ingredients, i)) for i in
                recipe_generator(len(ingredients), 100)
                if sum(i) == 100
            ]
        ])

    partb = max(
        [get_combined_score(recipe, ingredient_properties, target_calories=500) for recipe in
         [dict(zip(ingredients, i)) for i in
          recipe_generator(len(ingredients), 100)
          if sum(i) == 100
          ]
         ])
    return str(parta), str(partb)



if __name__ == "__main__":
    p = Puzzle(year=2015, day=15)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
