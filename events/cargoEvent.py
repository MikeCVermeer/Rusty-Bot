from .event import Event


async def cargoEvent(bot):
    cargo = await Event.createEventClass(bot, 5, True)
    return cargo.events
