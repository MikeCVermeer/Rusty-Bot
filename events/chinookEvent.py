from math import sqrt
from .event import Event
from mapmarkers import MapMarkers


async def chinookEvent(bot, rig):
    chinook = await Event.createEventClass(bot, 4, True)

    if rig == True:
        for chinook in chinook.events:
            check = await checkOilRig(bot, chinook)

            if check == "oil_rig_small":
                await bot.send_message(f"Small Oil Rig is active! <-- Rusty Bot")
                # chinook.grid = "Small Oil Rig"
            elif check == "large_oil_rig":
                await bot.send_message(f"Large Oil Rig is active! <-- Rusty Bot")
                # chinook.grid = "Large Oil Rig"
                return []
            else:
                return []

    return chinook.events

async def checkOilRig(bot, chinook):
    oilRigs = await MapMarkers.initialiseMapMarkers(bot)
    
    for oilRig in oilRigs.oilRigs:
        x = oilRig.x
        y = oilRig.y

        distance = sqrt((chinook.x - x)**2 + (chinook.y - y)**2)

        if distance <= 600:
            return oilRig.token