async def notificationHandlerEvents(bot, event, mapEvent = False, Update = False):
    if mapEvent == True:
        if event.grid == "Small Oil Rig":
            await notificationHandlerOilRigs(bot, event)
        elif event.grid == "Large Oil Rig":
            await notificationHandlerOilRigs(bot, event)
        else:
            await bot.send_message(f"Map event: {event.name} just spawned at: {event.grid}. A new {event.name} will spawn in roughly {event.respawnTime} minutes. <-- Rusty Bot")
    elif mapEvent == True and Update == True:
        await bot.send_message(f"Map event: {event.name} is currently located at: {event.grid} <-- Rusty Bot")

    return

async def notificationHandlerRaids(bot, raid):
    await bot.send_message(f"Raid zone detected at: {raid.grid} <-- Rusty Bot")

async def notificationHandlerOilRigs(bot, event):
    if event.grid == "Small Oil Rig":
        await bot.send_message(f"Small Oil Rig is active! <-- Rusty Bot")
    elif event.grid == "Large Oil Rig":
        await bot.send_message(f"Large Oil Rig is active! <-- Rusty Bot")
