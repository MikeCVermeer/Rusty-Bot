import json
import asyncio


async def getDurability(bot, args):
    item_name = " ".join(args)

    # Find item name in durability.json
    with open('durability.json') as f:
        data = json.load(f)

    # Find the requested structure in the json file
    for structure in data['structures']:
        if structure['name'].lower() == item_name.lower():
            structure_data = structure
            break
    else:
        await bot.send_message(f"Could not find durability data for item '{item_name}'. <-- Rusty Bot")
        return
    
    # Handle RaidMethods
    await getRaidMethods(bot, structure_data)


async def getRaidMethods(bot, structure_data):
    await bot.send_message(f"Raid methods for {structure_data['name']}:")
    for method in structure_data['raid_methods']:
        await bot.send_message(f"- {method['method']}: {method['sulfur_cost']} sulfur (x{method['amount']})")
    return


