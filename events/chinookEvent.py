from math import sqrt
from .event import Event
from mapmarkers import MapMarkers



async def chinookEvent(bot):
    chinook = await Event.createEventClass(bot, 4, True)

    for chinook in chinook.events:
        check = await checkOilRig(bot, chinook)

        if check == "oil_rig_small":
            chinook.grid = "Small Oil Rig"
            return chinook.events
        elif check == "large_oil_rig":
            chinook.grid = "Large Oil Rig"
            return chinook.events
        else:
            return chinook.events

async def checkOilRig(bot, chinook):
    oilRigs = await MapMarkers.initialiseMapMarkers(bot)
    
    for oilRig in oilRigs.oilRigs:
        x = oilRig.x
        y = oilRig.y

        distance = sqrt((chinook.x - x)**2 + (chinook.y - y)**2)

        if distance <= 600:
            return oilRig.token