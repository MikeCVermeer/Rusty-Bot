import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("firebase.auth.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def storePlayerData(playerData):
    steam_id = playerData.steam_id
    name = playerData.name
    xCords = playerData.x
    yCords = playerData.y
    is_online = playerData.is_online
    spawn_time = playerData.spawn_time
    is_alive = playerData.is_alive
    death_time = playerData.death_time

    data = {'steamId': steam_id, 'username': name, 'isOnline': is_online, 'spawnTime': spawn_time,
            'isAlive': is_alive, 'deathTime': death_time, 'cords': {'x': xCords, 'y': yCords}}

    # db.collection('playerData').add(data)

    return


def storeRaidData(raidData, raidTime):
    raid_id = raidData.id
    xCords = raidData.x
    yCords = raidData.y
    is_active = True

    data = {'startDate': raidTime, 'isActive': is_active, 'cords': {'x': xCords, 'y': yCords}}

    # db.collection('raids').document(str(raid_id)).set(data)

    return

def updateRaidData(raidData):
    raid_id = raidData.id
    is_active = False

    data = {'isActive': is_active}

    # db.collection('raids').document(str(raid_id)).set(data)

    return