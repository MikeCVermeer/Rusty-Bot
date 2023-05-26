import asyncio
import time
from mapevents import getMapEvents
from raidzones import getRaidZone
from notificationhandler import notificationHandlerEvents, notificationHandlerRaids
from events.event import Event
from events.chinookEvent import chinookEvent

async def listeners(bot):
    await asyncio.sleep(5)
    print("Listeners started")
    # Listener loop
    while True:
        # Check for events on the map
        await asyncio.gather(mapEventListener(bot), raidListener(bot), oilRigListener(bot))

        # Sleep for 10 seconds
        await asyncio.sleep(15)

    return

# List to hold the last map events we got
lastMapEvents = []

# Check for events on the map
async def mapEventListener(bot):
    mapEvents = await Event.createEventClass(bot)

    for mapEvent in mapEvents.events:
        # Look for this event in the list of past events
        for recordedEvent in lastMapEvents:
            if mapEvent.id == recordedEvent["event"].id:
                # The event is already in the list
                # Check if 15 minutes have passed
                if time.time() - recordedEvent["timestamp"] >= 15*60:
                    # 15 minutes have passed, send an update
                    await notificationHandlerEvents(bot, mapEvent, True, True)
                break
        else:
            # The event was not in the list, add it
            lastMapEvents.append({"event": mapEvent, "timestamp": time.time()})
            await notificationHandlerEvents(bot, mapEvent, True)

foundRaidZones = []

async def raidListener(bot):
    raids = await getRaidZone(bot)

    for raid in raids:
        # If the raid is not in the list, add it
        if raid not in foundRaidZones:
            foundRaidZones.append(raid)
            await notificationHandlerRaids(bot, raid)
        else:
            # The raid was already found, do nothing
            pass

    return

foundOilRigs = []

async def oilRigListener(bot):
    oilRigs = await chinookEvent(bot, True)
    if len(oilRigs) > 0:
        for oilRig in oilRigs:
            # If the oil rig is not in the list, add it
            if oilRig not in foundOilRigs:
                foundOilRigs.append(oilRig)
                await bot.send_message(f"{oilRig} active! <-- Rusty Bot")
            else:
                # The oil rig was already found, do nothing
                pass
    else:
        # There are no oil rigs active, do nothing
        pass

    return
