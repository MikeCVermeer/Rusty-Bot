import asyncio
import time
from databasehandler import updateRaidData
from mapevents import getMapEvents
from raidzones import getRaidZone
from notificationhandler import notificationHandlerEvents, notificationHandlerRaids
from events.event import Event
from events.chinookEvent import chinookEvent
from teaminfo import getTeamInfo


async def listeners(bot):
    await asyncio.sleep(5)
    print("Listeners started")
    # Listener loop
    while True:
        # Check for events on the map
        await asyncio.gather(mapEventListener(bot), raidListener(bot), teamListener(bot))

        # Sleep for 15 seconds
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
                    # 15 minutes have passed, send an update, and update the timestamp
                    await notificationHandlerEvents(bot, mapEvent, True, True)
                    recordedEvent["timestamp"] = time.time()
                break
        else:
            # The event was not in the list, add it
            lastMapEvents.append({"event": mapEvent, "timestamp": time.time()})
            await notificationHandlerEvents(bot, mapEvent, True)


activeRaidZones = []

async def newRaidListener(bot):
    raids = await getRaidZone(bot)

    for activeRaid in activeRaidZones:
        if activeRaid not in raids:
            # Raid is no longer active
            # TODO: Remove raid from array
            updateRaidData(activeRaid)
        else:
            # Raid is still active
            pass

    for newRaid in raids:
        # If the raid is not in the list, add it
        if newRaid not in activeRaidZones:
            activeRaidZones.append(newRaid)
            await notificationHandlerRaids(bot, newRaid)
        else:
            # The raid was already found in active raids
            pass

    return

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


async def teamListener(bot):
    teamData = await getTeamInfo(bot)

    return
