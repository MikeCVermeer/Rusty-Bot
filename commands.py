from rustplus import CommandOptions, Command, RustSocket
from mapevents import getMapEvents
from raidzones import getRaidZone
from timers import setTimer
from events.cargoEvent import cargoEvent
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
    async def version(command : Command):
        await bot.version()

    @bot.socket.command
    async def timer(command : Command):
        await setTimer(bot, command.args)

    @bot.socket.command
    async def help(command : Command):
        await bot.send_message("Rusty Bot commands:")
        await bot.send_message("- !help - Displays this message.")
        await bot.send_message("- !version - Displays the current version of Rusty Bot.")
        await bot.send_message("- !disconnect - Disconnects Rusty Bot from the server.")
        await bot.send_message("- !heli - Displays the current location of the Helicopter.")
        await bot.send_message("- !chinook - Displays the current location of the Chinook.")
        await bot.send_message("- !cargo - Displays the current location of the Cargoship.")
        await bot.send_message("- !raids - Displays all active raids on the map.")
        await bot.send_message("- !timer [<minutes>] <seconds> [<name>] - Sets a timer for the specified amount time.")
        await bot.send_message("- !pop - Displays the current server population.")

    # TODO: verify working of commands

    @bot.socket.command
    async def heli(command : Command):
        helis = await getMapEvents(bot.socket, True, 8)
        if len(helis) > 0:
            for heli in helis:
                await bot.send_message(f"A Helicopter is currently located at: {heli.grid} <-- Rusty Bot")
        else:
            await bot.send_message(f"There is no Helicopter active at this moment. <-- Rusty Bot")

    @bot.socket.command
    async def chinook(command : Command):
        chinooks = await getMapEvents(bot.socket, True, 4)
        if len(chinooks) > 0:
            for chinook in chinooks:
                await bot.send_message(f"A Chinook is currently located at: {chinook.grid} <-- Rusty Bot")
        else:
            await bot.send_message(f"There is no Chinook active at this moment. <-- Rusty Bot")

    @bot.socket.command
    async def cargo(command : Command):
        cargos = await getMapEvents(bot.socket, True, 5)
        if len(cargos) > 0:
            for cargo in cargos:
                await bot.send_message(f"A Cargoship is currently located at: {cargo.grid} <-- Rusty Bot")
        else:
            await bot.send_message(f"There is no Cargoship active at this moment. <-- Rusty Bot")

    @bot.socket.command
    async def raids(command : Command):
        raids = await getRaidZone(bot, True)
        if raids == False:
            await bot.send_message(f"There are no active raids at this moment. <-- Rusty Bot")

    @bot.socket.command
    async def events(command : Command):
        events = await getMapEvents(bot.socket, True)
        if len(events) > 0:
            for event in events:
                await bot.send_message(f"Event: {event.name} is currently located at: {event.grid} <-- Rusty Bot")
        else:
            await bot.send_message(f"There are no events active at this moment. <-- Rusty Bot")

    @bot.socket.command
    async def test(command : Command):
        event = await cargoEvent(bot)
        await bot.send_message(f"Event: {event.name} is currently located at: {event.grid} <-- Rusty Bot")
            