from mhw_api_wrapper.mhw_wrapper import MHWDBWrapper
from mhw_api_wrapper import items, monsters, ailments, armors
import asyncio

# Créez une instance de la classe MHWDBWrapper
mhw_api = MHWDBWrapper()

async def main():
    # Obtenez les détails de l'objet
    object_id = int(50)  # Remplacez par l'ID de l'objet souhaité
    object_details = await items.get_item_by_id(mhw_api, object_id)

    if object_details:
        print("ID de l'objet :", object_details.id)
        print("Nom de l'objet :", object_details.name)
        print("Description de l'objet :", object_details.description)
        print("Rareté de l'objet :", object_details.rarity)
        print("Limite de portée de l'objet :", object_details.carryLimit)
        print("Valeur de l'objet :", object_details.value)
    else:
        print("Objet non trouvé ou erreur de requête.")
async def monsterdetails():
    monster_id = 50
    monster_details = await monsters.get_monster_by_id(mhw_api, monster_id)

    if monster_details:
        print("Nom du monstre :", monster_details.name)
        print("Description du monstre :", monster_details.description)
        print("Faiblesses du monstre :", monster_details.weaknesses)
        print("Type du monstre :", monster_details.type)

async def armor():
    armor_id = 50
    armor_details = await armors.get_armor_by_id(mhw_api, armor_id)

    if armor_details:
        print("Details de l'armure :",armor_details.id)
asyncio.run(armor())