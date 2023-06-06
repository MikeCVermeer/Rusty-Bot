from databasehandler import storePlayerData


async def getTeamInfo(bot, command=False):
    # Get the team data from bot
    teamInfo = await bot.get_team_info()

    for member in teamInfo.members:
        storePlayerData(member)

    return teamInfo
