from rustplus import CommandOptions, Command, RustSocket
from mapevents import getMapEvents
from raidzones import getRaidZone
from timers import setTimer
from events.cargoEvent import cargoEvent
from events.chinookEvent import chinookEvent
from events.heliEvent import heliEvent
from mapmarkers import MapMarkers
from durability import getDurability
import asyncio


options = CommandOptions(prefix='!')

async def commandListener(bot):
    ### Help Commands ###
    @bot.socket.command(aliases=["commands"])
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
        await bot.send_message("- !events - Displays all active events on the map.")
        await bot.send_message("- !durability <structure> - Displays the raid methods for the specified structure.")
        await bot.send_message("- !pop - Displays the current server population.")

    ### General Commands ###
    @bot.socket.command
    async def disconnect(command : Command):
        await bot.disconnect()

    @bot.socket.command(aliases=["players", "population"])
    async def pop(command : Command):
        info = await bot.get_info()
        await bot.send_message(f"Current server population is: {info.players} / {info.max_players} players. <-- Rusty Bot")

    @bot.socket.command
    async def version(command : Command):
        await bot.version()



    ### Utility Commands ###
    @bot.socket.command(aliases=["timer", "timers"])
    async def timer(command : Command):
        await setTimer(bot, command.args)



    ### Map Event Commands ###
    @bot.socket.command(aliases=["helicopter", "patrolheli", "patrolhelicopter"])
    async def heli(command : Command):
        events = await heliEvent(bot)
        if len(events) > 0:
            for event in events:
                await bot.send_message(f"A Helicopter is currently located at: {event.grid} <-- Rusty Bot")
        else:
            await bot.send_message(f"There is no Helicopter active at this moment. <-- Rusty Bot")

    @bot.socket.command(aliases=["ch47"])
    async def chinook(command : Command):
        events = await chinookEvent(bot)
        # if len(events) > 0:
        if events != None:
            for event in events:
                await bot.send_message(f"A Chinook is currently located at: {event.grid} <-- Rusty Bot")
        else:
            await bot.send_message(f"There is no Chinook active at this moment. <-- Rusty Bot")

    @bot.socket.command(aliases=["cargoship", "ship"])
    async def cargo(command : Command):
        events = await cargoEvent(bot)
        if len(events) > 0:
            for event in events:
                await bot.send_message(f"Event: {event.name} is currently located at: {event.grid} <-- Rusty Bot")
        else:
            await bot.send_message(f"There is no Cargoship active at this moment. <-- Rusty Bot")

    @bot.socket.command(aliases=["raid", "raidzone", "raidzones"])
    async def raids(command : Command):
        raids = await getRaidZone(bot, True)
        if raids == False:
            await bot.send_message(f"There are no active raids at this moment. <-- Rusty Bot")

    @bot.socket.command(aliases=["event"])
    async def events(command : Command):
        events = await getMapEvents(bot.socket, True)
        if len(events) > 0:
            for event in events:
                await bot.send_message(f"Event: {event.name} is currently located at: {event.grid} <-- Rusty Bot")
        else:
            await bot.send_message(f"There are no events active at this moment. <-- Rusty Bot")



    ### Raid Commands ###
    @bot.socket.command(aliases=["dura", "raidcost"])
    async def durability(command : Command):
        await getDurability(bot, command.args)
