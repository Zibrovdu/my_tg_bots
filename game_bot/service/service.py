import random

from lexicon.lexicon import LEXICON


def bot_choice():
    return random.choice([LEXICON['stone'], LEXICON['paper'], LEXICON['scissors']])


async def get_winner(user_choice, bot):
    rules = {
        'stone': 'scissors',
        'paper': 'stone',
        'sclossors': 'paper'
    }
    if rules[user_choice] == bot:
        return 'user_win'
    return 'user_miss'
