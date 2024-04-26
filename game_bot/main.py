import asyncio

from aiogram import Bot, Dispatcher
from config.conf import Config, load_config
from handlers import user_handlers
from keyboards.kbrds import kb_builder, kb_game_builder


async def main() -> None:
    config: Config = load_config('.env')

    bot = Bot(token=config.bot.token)
    dp = Dispatcher()

    dp.include_router(user_handlers.r)

    kb = kb_builder
    kb_game = kb_game_builder

    dp.workflow_data.update({'kb': kb, 'kb_game': kb_game})

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
