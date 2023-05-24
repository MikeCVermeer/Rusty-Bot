async def notificationHandlerEvents(bot, event, mapEvent = False, Update = False):
    if mapEvent == True:
        await bot.send_message(f"Map event: {event.name} just spawned at: {event.grid}. A new {event.name} will spawn in roughly {event.respawnTime} minutes. <-- Rusty Bot")
    elif mapEvent == True and Update == True:
        await bot.send_message(f"Map event: {event.name} is currently located at: {event.grid} <-- Rusty Bot")

    return

async def notificationHandlerRaids(bot, raid):
    await bot.send_message(f"Raid zone detected at: {raid.grid} <-- Rusty Bot")
