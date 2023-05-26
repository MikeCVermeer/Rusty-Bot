from .event import Event


async def chinookEvent(bot):
    chinook = await Event.createEventClass(bot, 4, True)
    return chinook.events
