import asyncio
from rustplus import RustSocket, CommandOptions
import listeners
import commands

class RustyBot:
    def __init__(self, ip, port, steamid, playertoken, command_options):
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
            await self.socket.send_team_message("Rusty Bot is awake! <-- RustyBot")
        except Exception as e:
            print(f"Rusty Bot failed to connect to server. \nError: {e}")

    async def send_message(self, message):
        await self.socket.send_team_message(message)

    async def disconnect(self):
        print("Rusty Bot disconnecting from server")
        await self.socket.send_team_message("Rusty Bot going to sleep... <-- RustyBot")
        await self.socket.disconnect()
        exit()

    async def version(self):
        version = "V0.1.2 [ALPHA]"
        print(f"Rusty Bot version: {version}")
        await self.socket.send_team_message(f"Rusty Bot version: {version} <-- RustyBot")

    async def listen(self):
        await listeners.listeners(self)

    async def get_raw_map_data(self):
        return await self.socket.get_raw_map_data()
    
    async def get_map_markers(self):
        return await self.socket.get_markers()
    
    async def get_info(self):
        return await self.socket.get_info()
    
    async def get_current_events(self):
        return await self.socket.get_current_events()

async def main():
    options = CommandOptions(prefix='!')
    bot = RustyBot('192.248.164.111', '28088', 76561198205490971, -1577019259, command_options=options)
    await bot.connect()

    # Start listening
    await asyncio.gather(bot.listen(), listeners.raidListener(bot), commands.commandListener(bot))
    
    await bot.disconnect()

asyncio.run(main())