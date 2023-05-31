import asyncio
import logging
import math
import string

class Event:
    def __init__(self, bot, event, command = False):
        self.bot = bot
        self.command = command
        self.event = event
        self.gridSize = 150
        self.name = self.getEventName(eventType = self.event)
        self.respawnTime = self.getRespawnTime(eventType = self.event)

    @classmethod
    async def createEventClass(cls, bot, event = None, command = False):
        self = Event(bot, event, command)
        self.events = await self.getMapEvents()
        return self

    def getEventName(self, eventType):
        typeToName = {
            2: "Bradley",
            4: "Chinook",
            5: "Cargo Ship",
            6: "Crate",
            8: "Patrol Helicopter",
        }

        return typeToName.get(eventType, "Unknown name")
    
    def getRespawnTime(self, eventType):
        TypeToRespawnTime = {
            2: None,
            4: 90,
            5: 30,
            6: None,
            8: 90,
        }

        return TypeToRespawnTime.get(eventType, None)
    
    async def getMapEvents(self):
        events = await self.bot.get_current_events()

        # If we didn't get any events
        if not events:
            return events
        
        if self.command == True:
            # Get the event type
            if self.event == None:
                # No event type was specified
                print("ERROR: No event type was specified")
                return events
            else:
                # Filter the events by type
                events = [event for event in events if event.type == self.event]

        # Print out the events we got - for testing purposes
        for event in events:
            event.name = self.getEventName(event.type)

            # Get the event location
            grid = await self.determineEventLocation(self.bot, event.x, event.y)

            event.grid = grid
            event.respawnTime = self.getRespawnTime(event.type)

            # Prints all events - for testing purposes
            # logging.log(f"Event name: {event.name}, Event type: {event.type}, Event position: {event.x}, {event.y}, Event id: {event.id} Event Location: {grid}")

        return events
    
    async def determineEventLocation(self, bot, eventX, eventY):
        # Get the map data
        gameMap = await bot.get_raw_map_data()

        # Get the map dimensions
        mapMargin = gameMap.margin
        mapHeight = gameMap.height - (2 * mapMargin) 
        mapWidth = gameMap.width - (2 * mapMargin)
        mapSize = mapWidth + mapHeight

        x = eventX
        y = mapSize - eventY

        if x < 0 or x >= mapSize or y < 0 or y >= mapSize:
            return self.calculateQuadrant(mapWidth, mapHeight, x, y)
        
        return self.calculateGrid(x, y)
    
    def calculateGrid(self, x, y):
        gridX = string.ascii_uppercase[math.floor(x / self.gridSize)]
        gridY = math.floor(y / self.gridSize)
        return f"{gridX}{gridY}"
    
    def calculateQuadrant(self, mapWidth, mapHeight, eventX, eventY):
        thirdX = mapWidth / 3
        twoThirdX = thirdX * 2
        thirdY = mapHeight / 3
        twoThirdY = thirdY * 2

        if thirdX <= eventX <= twoThirdX and thirdY <= eventY <= twoThirdY:
            return "Inside Grid"
        
        if eventX < thirdX:
            if eventY < thirdY:
                return "Top left quadrant"
            elif eventY <= twoThirdY:
                return "Left center quadrant"
            else:
                return "Bottom left quadrant"
            
        elif eventX <= twoThirdX:
            if eventY < thirdY:
                return "Top center quadrant"
            else:
                return "Bottom center quadrant"
            
        else:
            if eventY < thirdY:
                return "Top right quadrant"
            elif eventY <= twoThirdY:
                return "Right center quadrant"
            else:
                return "Bottom right quadrant"
