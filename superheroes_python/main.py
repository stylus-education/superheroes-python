from superheroes_python.get_characters import get_characters


def battle(hero_name, villain_name):
    characters = get_characters()

    hero = None
    villain = None

    for character in characters["items"]:
        if character["name"] == hero_name:
            hero = character
        if character["name"] == villain_name:
            villain = character

    return hero if hero["score"] >= villain["score"] else villain
