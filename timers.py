import asyncio


async def timerTask(bot, total_seconds, name):
    await asyncio.sleep(total_seconds)
    prefix = "Timer" if name == "Timer" else f"Timer '{name}'"
    await bot.send_message(f"Ring ring ring ring ring ring ring, banana phone! {prefix} expired. <-- Rusty Bot")

async def setTimer(bot, args):
    if len(args) < 1:
        await bot.send_message("Timer usage: !timer [<minutes>] <seconds> [<name>].")
        await bot.send_message("Minutes are optional, if given only one argument it will be interpreted as seconds. Name is optional.")
        await bot.send_message("Example: !timer 15 00 Locked Crate - This will set a timer called 'Locked Crate' for 15 minutes. <-- Rusty Bot")
        return

    try:
        if len(args) == 1:
            # Only seconds were provided
            total_seconds = int(args[0])
            name = "Timer"
        elif args[1].isdigit():
            minutes = int(args[0])
            seconds = int(args[1])
            total_seconds = minutes * 60 + seconds
            name = " ".join(args[2:]) if len(args) > 2 else "Timer"
        else:
            total_seconds = int(args[0])
            name = " ".join(args[1:])
    except ValueError:
        await bot.send_message("Invalid arguments. Both minutes and seconds should be numbers. <-- Rusty Bot")
        return

    if total_seconds > 30 * 60:
        await bot.send_message("Error: Maximum timer duration is 30 minutes. <-- Rusty Bot")
        return

    # Convert total_seconds to minutes and seconds
    minutes, seconds = divmod(total_seconds, 60)

    asyncio.create_task(timerTask(bot, total_seconds, name))
    msg_prefix = f"Timer: '{name}'" if name != "Timer" else "Timer"
    await bot.send_message(f"{msg_prefix} set for {minutes} minutes and {seconds} seconds. <-- Rusty Bot")

    return