import asyncio

from loguru import logger

from tgbot import handlers, utils
from tgbot.loader import bot, dp


async def main():
    utils.setup_logger("INFO", ["sqlalchemy.engine", "aiogram.bot.api"])

    dp.include_routers(handlers.default_router)

    try:
        logger.info("Start polling...")
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        logger.info("Close bot session...")
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        exit()
