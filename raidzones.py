import math
import string


async def getRaidZone(bot):
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

    # Filter markers of type 7 and compute grid coordinates
    filtered_markers = []
    for marker in markers:
        if marker.type != 7:
            continue

        x = marker.x
        y = mapSize - marker.y

        if x < 0 or x >= mapSize or y < 0 or y >= mapSize:
            continue  # skip this marker as it's outside map

        # Calculate the grid coordinates
        gridX = string.ascii_uppercase[math.floor(x / gridSize)]
        gridY = math.floor(y / gridSize) + 1

        # Combine the grid coordinates
        grid = f"{gridX}{gridY - 1}"

        # assign the grid to marker
        marker.grid = grid
        
        # append this marker to filtered_markers
        filtered_markers.append(marker)

    return filtered_markers