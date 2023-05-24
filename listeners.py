import asyncio
import time
from mapevents import getMapEvents
from raidzones import getRaidZone
from notificationhandler import notificationHandlerEvents, notificationHandlerRaids
from timers import timer

async def listeners(bot):
    print("Listeners started")
    # Listener loop
    while True:
        # Check for events on the map
        await asyncio.gather(mapEventListener(bot), raidListener(bot), timerListener(bot))

        # Sleep for 10 seconds
        await asyncio.sleep(10)

    return

# Timer listener
async def timerListener(bot):
    # Check if a timer has expired
    await timer(bot)

    return

# List to hold the last map events we got
lastMapEvents = []

# Check for events on the map
async def mapEventListener(bot):
    mapEvents = await getMapEvents(bot.socket)

    for mapEvent in mapEvents:
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