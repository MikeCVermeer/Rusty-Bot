import asyncio
from mapevents import getMapEvents
import commands
from notificationhandler import notificationHandler

async def listeners(bot):
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
        # If we haven't seen this event before
        if mapEvent.id not in lastMapEvents:
            print(f"New event: {mapEvent.id}")
            lastMapEvents.append(mapEvent.id)

            await notificationHandler(bot, mapEvent, True)
            
        else:
            print(f"Event already seen: {mapEvent.id}")


    return