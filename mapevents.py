import string


async def getMapEvents(bot, command = False):
    events = await bot.get_current_events()

    # A dictionary of event types to their names
    typeToName = {
        2: "Bradley",
        4: "Chinook",
        5: "Cargo Ship",
        6: "Crate",
        8: "Patrol Helicopter",
    }

    TypeToRespawnTime = {
        2: None,
        4: None,
        5: 30,
        6: None,
        8: 120,
    }

    # If we didn't get any events
    if len(events) == 0:
        # print("No events found")
        return events # Gives error currently.

    # Print out the events we got - for testing purposes
    for event in events:
        event.name = typeToName.get(event.type, "Unknown name")

        # Get the event location
        grid = await determineEventLocation(bot, event.x, event.y)

        event.grid = grid
        event.respawnTime = TypeToRespawnTime.get(event.type, None)

        print(f"Event name: {event.name}, Event type: {event.type}, Event position: {event.x}, {event.y}, Event id: {event.id} Event Location: {grid}")

    return events


    # # Calculate midpoints
    # midX = mapWidth / 2
    # midY = mapHeight / 2

    # # Determine the quadrant
    # if eventX < midX:
    #     if eventY > midY:
    #         return "Top Left of the map"
    #     else:
    #         return "Bottom Left of the map"
    # else:
    #     if eventY > midY:
    #         return "Top Right of the map"
    #     else:
    #         return "Bottom Right of the map"

    # print (f"Event position: {eventX}, {eventY}")
    # print (f"Map dimensions: {mapWidth}, {mapHeight}")
    
async def determineEventLocation(bot, eventX, eventY):
    # Get the map data
    gameMap = await bot.get_raw_map_data()

    # Get the map dimensions
    mapMargin = gameMap.margin
    mapHeight = gameMap.height - (2 * mapMargin) 
    mapWidth = gameMap.width - (2 * mapMargin)

    # # Grid size
    # gridSize = 150

    # # Calculate the grid position, converting in-game coords to code coords. 
    # gridX = int((eventX + mapWidth / 2) / gridSize) + 1
    # gridY = int((mapHeight / 2 - eventY) / gridSize)

    # # Convert to Rust's grid system.
    # if gridY < 26:
    #     gridLetter = string.ascii_uppercase[gridY]  # This will get the letter equivalent of the gridY value.
    # else:
    #     gridLetter = string.ascii_uppercase[gridY // 26 - 1] + string.ascii_uppercase[gridY % 26]

    # gridNumber = gridX

    # print (f"Event position: {eventX}, {eventY}")
    # print (f"Map dimensions: {mapWidth}, {mapHeight}")
    # print (f"Grid position: {gridX}, {gridY}")
    # print (f"Grid position: {gridLetter}, {gridNumber}")

    # return f"{gridLetter}{gridNumber}"

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