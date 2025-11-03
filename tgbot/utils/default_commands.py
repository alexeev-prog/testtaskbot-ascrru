from aiogram.types import BotCommand, BotCommandScopeDefault


async def setup_default_commands(bot):
    commands = [
        BotCommand(command="start", description="Главное меню"),
        BotCommand(command="services", description="Услуги компании"),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
