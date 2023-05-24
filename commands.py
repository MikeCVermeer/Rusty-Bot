from rustplus import CommandOptions, Command, RustSocket
from mapevents import getMapEvents
import asyncio


options = CommandOptions(prefix='!')

async def commandListener(bot):

    @bot.socket.command
    async def disconnect(command : Command):
        await bot.disconnect()

    @bot.socket.command
    async def pop(command : Command):
        info = await bot.get_info()
        await bot.send_message(f"Current server population is: {info.players} / {info.max_players} players. <-- Rusty Bot")

    @bot.socket.command
    async def heli(command : Command):
        helis = await getMapEvents(bot.socket, True, 8)
        for heli in helis:
            if heli:
                await bot.send_message(f"A Helicopter is currently located at: {heli.grid} <-- Rusty Bot")
            else:
                await bot.send_message(f"There is no Helicopter active at this moment. <-- Rusty Bot")

    @bot.socket.command
    async def chinook(command : Command):
        chinooks = await getMapEvents(bot.socket, True, 4)
        for chinook in chinooks:
            if chinook:
                await bot.send_message(f"A Chinook is currently located at: {chinook.grid} <-- Rusty Bot")
            else:
                await bot.send_message(f"There is no Chinook active at this moment. <-- Rusty Bot")

    @bot.socket.command
    async def cargo(command : Command):
        cargos = await getMapEvents(bot.socket, True, 5)
        for cargo in cargos:
            if cargo:
                await bot.send_message(f"A Cargoship is currently located at: {cargo.grid} <-- Rusty Bot")
            else:
                await bot.send_message(f"There is no Cargoship active at this moment. <-- Rusty Bot")