import asyncio
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
    async def createEventClass(cls, bot, event, command = False):
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
            8: 120,
        }

        return TypeToRespawnTime.get(eventType, None)
    
    async def getMapEvents(self):
        events = await self.bot.get_current_events()

        # If we didn't get any events
        if len(events) == 0:
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

            print(f"Event name: {event.name}, Event Location: {grid}")

            event.grid = grid
            event.respawnTime = self.getRespawnTime(event.type)

            # Prints all events - for testing purposes
            # print(f"Event name: {event.name}, Event type: {event.type}, Event position: {event.x}, {event.y}, Event id: {event.id} Event Location: {grid}")

        return events
    
    async def determineEventLocation(self, bot, eventX, eventY):
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
