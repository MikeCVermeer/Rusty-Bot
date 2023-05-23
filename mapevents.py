async def getMapEvents(rust_socket):
    events = await rust_socket.get_current_events()

    for event in events:
        print(f"Event name: {event.name}, Event type: {event.type}, Event position: {event.rotation}")

    return events