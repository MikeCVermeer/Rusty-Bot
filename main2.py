import asyncio
from rustplus import RustSocket

IP = '192.248.164.111'
PORT = "28088"
STEAMID = 76561198205490971
PLAYERTOKEN = 1102527508

async def main():
    socket = RustSocket(IP, PORT, STEAMID, PLAYERTOKEN)
    await socket.connect()

    await socket.send_team_message("Rusty Bot connection established!")

    await socket.disconnect()

asyncio.run(main())