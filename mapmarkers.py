import math
import string


async def getMarkers(bot):
    # Get the map data
    gameMap = await bot.get_raw_map_data()

    # Get the map dimensions
    mapMargin = gameMap.margin
    mapHeight = gameMap.height - (2 * mapMargin) 
    mapWidth = gameMap.width - (2 * mapMargin)

    # Grid size
    gridSize = 150
    mapSize = mapWidth + mapHeight

    # Get the map markers
    markers = await bot.get_map_markers()

    # Loop through the markers
    for marker in markers:
        x = marker.x
        y = mapSize - marker.y

        print (f"{marker.name}, Type: {marker.type}, X: {marker.x}, Y: {marker.y} ID: {marker.id}")

        if x < 0 or x >= mapSize or y < 0 or y >= mapSize:
            return "Outside map"

        # Calculate the grid coordinates
        gridX = string.ascii_uppercase[math.floor(x / gridSize)]
        gridY = math.floor(y / gridSize) + 1

    # Combine the grid coordinates
        grid = f"{gridX}{gridY - 1}"

        marker.grid = grid

        # print(f"Marker name: {marker.name}, Marker Location: {grid}")

    return markers