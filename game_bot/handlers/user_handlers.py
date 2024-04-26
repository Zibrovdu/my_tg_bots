import random

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import LEXICON
from service.service import bot_choice, get_winner

r = Router()


@r.message(CommandStart())
async def start_command(message: Message, kb: ReplyKeyboardBuilder):
    await message.answer(
        text=LEXICON['/start'],
        reply_markup=kb.as_markup(
            resize_keyboard=True,
            one_time_keyboard=True)
    )


@r.message(Command(commands='help'))
async def help_cmd(message: Message, kb: ReplyKeyboardBuilder):
    await message.answer(
        text=LEXICON['/help'],
        reply_markup=kb.as_markup(
            resize_keyboard=True,
            one_time_keyboard=True)
    )


@r.message(lambda msg: msg.text == LEXICON['yes_btn'])
async def user_answer_yes(message: Message, kb_game: ReplyKeyboardBuilder):
    await message.answer(
        text=LEXICON['yes_user'],
        reply_markup=kb_game.as_markup(
            resize_keyboard=True,
            one_time_keyboard=True))


@r.message(lambda msg: msg.text in [LEXICON['stone'], LEXICON['paper'], LEXICON['scissors']])
async def user_in_game(message: Message, kb: ReplyKeyboardBuilder):
    bot = bot_choice()
    if bot == message.text:
        await message.answer(
            text=LEXICON['draw'],
            reply_markup=kb.as_markup(
                resize_keyboard=True,
                one_time_keyboard=True))
    else:
        if get_winner(message.text, bot) == 'user_win':
            await message.answer(
                text=LEXICON['user_win']
            )
        else:
            await message.answer(text=LEXICON['user_miss'])

    await message.answer(
        text=f'Пользователь выбрал: {message.text}, бот выбрал: {bot}'
    )
    await message.answer(
        text=LEXICON['new_game'],
        reply_markup=kb.as_markup(
            resize_keyboard=True,
            one_time_keyboard=True)
    )


@r.message(lambda msg: msg.text == LEXICON['no_btn'])
async def user_answer_no(message: Message, kb: ReplyKeyboardBuilder):
    await message.answer(
        text=LEXICON['no_user'])


@r.message()
async def any_message(message: Message):
    await message.answer(text=LEXICON['undefine'])
