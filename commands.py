from rustplus import CommandOptions, Command, RustSocket
import asyncio



options = CommandOptions(prefix='!')

bot = None
async def commandListener(bot):
    bot = bot

    @bot.command
    async def disconnect(command : Command):
        await bot.disconnect()
