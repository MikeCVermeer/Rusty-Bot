async def notificationHandler(bot, event, mapEvent = False):
    print("Notification handler called")
    if mapEvent == True:
        print("Event is true")
        
        await bot.send_message(f"New event: {event.name} at {event.x}, {event.y}")


    return