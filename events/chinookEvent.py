from math import sqrt
from .event import Event
from mapmarkers import MapMarkers


async def chinookEvent(bot, rig):
    chinook = await Event.createEventClass(bot, 4, True)

    if rig == True:
        for chinook in chinook.events:
            check = await checkOilRig(bot, chinook)

            if check == "oil_rig_small":
                return "Small Oil Rig"
            elif check == "large_oil_rig":
                return "Large Oil Rig"
            else:
                return []

    return chinook.events

async def checkOilRig(bot, chinook):
    oilRigs = await MapMarkers.initialiseMapMarkers(bot)
    
    for oilRig in oilRigs.oilRigs:
        x = oilRig.x
        y = oilRig.y

        distance = sqrt((chinook.x - x)**2 + (chinook.y - y)**2)

        if distance <= 400:
            return oilRig.token