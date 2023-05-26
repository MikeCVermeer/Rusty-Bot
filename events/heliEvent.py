from .event import Event


async def heliEvent(bot):
    heli = await Event.createEventClass(bot, 8, True)
    return heli.events
