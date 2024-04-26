import random

from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import LEXICON

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
    bot_choice = random.choice([LEXICON['stone'], LEXICON['paper'], LEXICON['scissors']])
    if bot_choice == message.text:
        await message.answer(
            text=LEXICON['draw'],
            reply_markup=kb.as_markup(
                resize_keyboard=True,
                one_time_keyboard=True))
    else:
        if (
                message.text == LEXICON['stone'] and bot_choice == LEXICON['scissors']) or (
                message.text == LEXICON['paper'] and bot_choice == LEXICON['stone']) or (
                message.text == LEXICON['scissors'] and bot_choice == LEXICON['paper']):
            await message.answer(
                text=LEXICON['user_win']
            )
        else:
            await message.answer(text=LEXICON['user_miss'])

    await message.answer(
        text=f'Пользователь выбрал: {message.text}, бот выбрал: {bot_choice}'
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
