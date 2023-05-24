import asyncio
from rustplus import RustSocket
import listeners
import commands

class RustyBot:
    def __init__(self, ip, port, steamid, playertoken):
        self.ip = ip
        self.port = port
        self.steamid = steamid
        self.playertoken = playertoken
        self.socket = RustSocket(self.ip, self.port, self.steamid, self.playertoken)

    async def connect(self):
        try:
            await self.socket.connect()
            print("Rusty Bot connected to server")
            await self.socket.send_team_message("Rusty Bot is awake! <-- RustyBot")
        except Exception as e:
            print(f"Rusty Bot failed to connect to server. \nError: {e}")

    async def send_message(self, message):
        await self.socket.send_team_message(message)

    async def disconnect(self):
        print("Rusty Bot disconnecting from server")
        await self.socket.send_team_message("Rusty Bot going to sleep... <-- RustyBot")
        await self.socket.disconnect()

    async def listen(self):
        await listeners.listeners(self)

    async def get_raw_map_data(self):
        return await self.socket.get_raw_map_data()
    
    async def get_map_markers(self):
        return await self.socket.get_markers()

async def main():
    bot = RustyBot('192.248.164.111', '28088', 76561198205490971, 1102527508)
    await bot.connect()

    # Initialize commands
    # await commands.commandListener(bot)

    # Start listening
    # await bot.listen()
    # await listeners.listeners(bot)
    await asyncio.gather(bot.listen(), listeners.markerListener(bot))
    
    await bot.disconnect()

asyncio.run(main())