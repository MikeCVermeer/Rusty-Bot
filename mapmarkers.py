import math
import string
import asyncio


class MapMarkers:
    def __init__(self, bot):
        self.bot = bot
        self.gridSize = 150

    @classmethod
    async def initialiseMapMarkers(cls, bot, marker = None):
        self = MapMarkers(bot)
        self.marker = marker
        self.mapData = await self.bot.get_raw_map_data()
        self.mapMargin = self.mapData.margin
        self.mapHeight = self.mapData.height - (2 * self.mapMargin)
        self.mapWidth = self.mapData.width - (2 * self.mapMargin)
        self.mapSize = self.mapWidth + self.mapHeight
        self.markers = await self.getFilteredMarkers(marker)
        self.monuments = await self.getMonuments()
        self.oilRigs = await self.getOilRigs()
        return self

    async def getFilteredMarkers(self, marker):
        markers = await self.bot.get_map_markers()
        filteredMarkers = []
        for marker in markers:
            x = marker.x
            y = self.mapSize - marker.y

            if x < 0 or x >= self.mapSize or y < 0 or y >= self.mapSize:
                continue  # skip this marker as it's outside map

            # Calculate the grid coordinates
            gridX = string.ascii_uppercase[math.floor(x / self.gridSize)]
            gridY = math.floor(y / self.gridSize)

            # Combine the grid coordinates
            grid = f"{gridX}{gridY}"

            # assign the grid to marker
            marker.grid = grid
            filteredMarkers.append(marker)
            
        return filteredMarkers
    
    async def getMonuments(self):
        monuments = self.mapData.monuments
        return monuments
    
    async def getOilRigs(self):
        monuments = self.mapData.monuments
        
        oilRigs = []
        for monument in monuments:
            if monument.token == "oil_rig_small" or monument.token == "large_oil_rig":
                oilRigs.append(monument)

        return oilRigs