from .event import Event


async def cargoEvent(bot):
    cargo = Event(bot, 5)
    await cargo.getMapEvents()
    return cargo
