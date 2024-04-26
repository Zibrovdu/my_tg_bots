from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON


buttons: list[KeyboardButton] = [
    KeyboardButton(text=LEXICON['yes_btn']),
    KeyboardButton(text=LEXICON['no_btn'])
]

kb_builder = ReplyKeyboardBuilder()
kb_builder.row(*buttons)


game_buttons: list[KeyboardButton] = [
    KeyboardButton(text=LEXICON['stone']),
    KeyboardButton(text=LEXICON['scissors']),
    KeyboardButton(text=LEXICON['paper'])
]

kb_game_builder = ReplyKeyboardBuilder()
kb_game_builder.row(*game_buttons)
