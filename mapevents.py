async def getMapEvents(rust_socket, command = False):
    events = await rust_socket.get_current_events()

    # A dictionary of event types to their names
    typeToName = {
        2: "Bradley",
        4: "Chinook",
        5: "Cargo Ship",
        6: "Crate",
        8: "Patrol Helicopter",
    }

    # If we didn't get any events
    if len(events) == 0:
        print("No events found")
        return events # Gives error currently.

    # Print out the events we got - for testing purposes
    for event in events:
        event.name = typeToName.get(event.type, "Unknown name")
        print(f"Event name: {event.name}, Event type: {event.type}, Event position: {event.x}, {event.y}, Event id: {event.id}")

    return events