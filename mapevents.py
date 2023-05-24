import math
import string


async def getMapEvents(bot, command = False, type = None):
    events = await bot.get_current_events()

    # A dictionary of event types to their names
    typeToName = {
        2: "Bradley", # (explosions) Currently disabled
        4: "Chinook",
        5: "Cargo Ship",
        6: "Crate", # Currently disabled
        8: "Patrol Helicopter",
    }

    TypeToRespawnTime = {
        2: None,
        4: 90,
        5: 30,
        6: None,
        8: 120,
    }

    # If we didn't get any events
    if len(events) == 0:
        return events
    
    if command == True:
        # Get the event type
        if type == None:
            # No event type was specified
            print("ERROR: No event type was specified")
            return events
        else:
            # Filter the events by type
            events = [event for event in events if event.type == type]

    # Print out the events we got - for testing purposes
    for event in events:
        event.name = typeToName.get(event.type, "Unknown name")

        # Get the event location
        grid = await determineEventLocation(bot, event.x, event.y)

        event.grid = grid
        event.respawnTime = TypeToRespawnTime.get(event.type, None)

        print(f"Event name: {event.name}, Event type: {event.type}, Event position: {event.x}, {event.y}, Event id: {event.id} Event Location: {grid}")

    return events
    
async def determineEventLocation(bot, eventX, eventY):
    # Get the map data
    gameMap = await bot.get_raw_map_data()

    # Get the map dimensions
    mapMargin = gameMap.margin
    mapHeight = gameMap.height - (2 * mapMargin) 
    mapWidth = gameMap.width - (2 * mapMargin)

    # Grid size
    gridSize = 150
    mapSize = mapWidth + mapHeight

    x = eventX
    y = mapSize - eventY

    if x < 0 or x >= mapSize or y < 0 or y >= mapSize:
        # Calculate midpoints
        midX = mapWidth / 2
        midY = mapHeight / 2

        # Determine the quadrant
        if eventX < midX:
            if eventY > midY:
                return "Top Left of the map"
            else:
                return "Bottom Left of the map"
        else:
            if eventY > midY:
                return "Top Right of the map"
            else:
                return "Bottom Right of the map"

    # Calculate the grid coordinates
    gridX = string.ascii_uppercase[math.floor(x / gridSize)]
    gridY = math.floor(y / gridSize) + 1

    # Combine the grid coordinates
    grid = f"{gridX}{gridY - 1}"

    return grid