import random

fatal_bullet = random.randint(1, 7)


def roulette():
    bullet = random.randint(1, 7)
    if bullet == fatal_bullet:
        return 'Вы проиграли!'
    else:
        return 'Вы выжили!'
