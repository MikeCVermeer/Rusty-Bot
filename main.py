import asyncio
from rustplus import RustSocket
from mapevents import getMapEvents
import listeners

class RustyBot:
    def __init__(self, ip, port, steamid, playertoken):
        self.ip = ip
        self.port = port
        self.steamid = steamid
        self.playertoken = playertoken
        self.socket = RustSocket(self.ip, self.port, self.steamid, self.playertoken)

    async def connect(self):
        await self.socket.connect()

    async def send_message(self, message):
        await self.socket.send_team_message(message)

    async def disconnect(self):
        await self.socket.disconnect()

    async def listen(self):
        await self.socket.listen()

async def main():
    bot = RustyBot('192.248.164.111', '28088', 76561198205490971, 1102527508)
    await bot.connect()
    # await bot.send_message("Rusty Bot connection established!")
    
    # events = await getMapEvents(bot.socket)

    # Run listeners
    await listeners.listeners(bot)
    
    await bot.disconnect()

asyncio.run(main())