import asyncio
from rustplus import RustSocket, CommandOptions
import listeners
import commands

class RustyBot:
    def __init__(self, ip, port, steamid, playertoken, command_options):
        self.versionNumber = "V0.3.3 [ALPHA]"
        self.ip = ip
        self.port = port
        self.steamid = steamid
        self.playertoken = playertoken
        self.command_options = command_options
        self.socket = RustSocket(self.ip, self.port, self.steamid, self.playertoken, self.command_options)

    async def connect(self):
        try:
            await self.socket.connect()
            print("Rusty Bot connected to server")
            print(f"Running Rusty Bot version: {self.versionNumber}")
            await self.socket.send_team_message("Rusty Bot is waking up! <-- RustyBot")
            await asyncio.sleep(3)
        except Exception as e:
            print(f"Rusty Bot failed to connect to server. \nError: {e}")

    async def send_message(self, message):
        await self.socket.send_team_message(message)

    async def disconnect(self):
        print("Rusty Bot disconnecting from server")
        await self.socket.send_team_message("Rusty Bot going to sleep... <-- RustyBot")
        # End all tasks
        for task in asyncio.all_tasks():
            task.cancel()
        await self.socket.disconnect()
        exit()

    async def version(self):
        print(f"Rusty Bot version: {self.versionNumber}")
        await self.socket.send_team_message(f"Rusty Bot version: {self.versionNumber} <-- RustyBot")

    async def listen(self):
        # await listeners.listeners(self)
        await asyncio.gather(listeners.listeners(self), listeners.raidListener(self), commands.commandListener(self))

    async def get_raw_map_data(self):
        return await self.socket.get_raw_map_data()
    
    async def get_map_markers(self):
        return await self.socket.get_markers()
    
    async def get_info(self):
        return await self.socket.get_info()
    
    async def get_current_events(self):
        return await self.socket.get_current_events()
    
    async def get_team_info(self):
        return await self.socket.get_team_info()

async def main():
    options = CommandOptions(prefix='!')
    bot = RustyBot('192.248.164.111', '28088', 76561198205490971, 245608122, command_options=options)
    await bot.connect()

    # Start listening
    await asyncio.gather(bot.listen())
    
    await bot.disconnect()

asyncio.run(main())