import asyncio
from rustplus import RustSocket

IP = '192.248.164.111'
PORT = "28088"
STEAMID = 76561198205490971
PLAYERTOKEN = 1102527508

async def main():
    socket = RustSocket(IP, PORT, STEAMID, PLAYERTOKEN)
    await socket.connect()

    print(f"Server name: {await socket.get_info()}")

    print(f"It is {(await socket.get_time()).time}")

    await socket.disconnect()

asyncio.run(main())