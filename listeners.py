import asyncio
import time
from mapevents import getMapEvents
import commands
from notificationhandler import notificationHandler

async def listeners(bot):
    print("Listeners started")
    # Listener loop
    while True:
        # Check for events on the map
        await mapEventListener(bot)

        # Sleep for 10 seconds
        await asyncio.sleep(10)

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
                    await notificationHandler(bot, mapEvent, True, True)
                break
        else:
            # The event was not in the list, add it
            lastMapEvents.append({"event": mapEvent, "timestamp": time.time()})
            await notificationHandler(bot, mapEvent, True)