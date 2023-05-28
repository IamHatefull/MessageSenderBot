from aiogram import Bot
from aiogram.types import  BotCommand, BotCommandScopeDefault

# Commands in bot menu
async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Start of work'
        ),
        BotCommand(
            command='help',
            description='Show help'
        ),
        BotCommand(
            command='show',
            description='Show keyboard'
        ),
        BotCommand(
            command='inline',
            description='Inline keyboard'
        ),
        BotCommand(
            command='form',
            description='Start quiz'
        ),
        BotCommand(
            command='cancel',
            description='Cancel'
        )
    ]

    await bot.set_my_commands(commands=commands)