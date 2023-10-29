from mhw_api_wrapper.mhw_wrapper import MHWDBWrapper
from mhw_api_wrapper.item import get_item_by_id
import asyncio

# Créez une instance de la classe MHWDBWrapper
mhw_api = MHWDBWrapper()

async def main():
    # Obtenez les détails de l'objet
    object_id = 50  # Remplacez par l'ID de l'objet souhaité
    object_details = await get_item_by_id(mhw_api, object_id)

    if object_details:
        print("ID de l'objet :", object_details.id)
        print("Nom de l'objet :", object_details.name)
        print("Description de l'objet :", object_details.carryLimit)
        print("Rareté de l'objet :", object_details.rarity)
        print("Limite de portée de l'objet :", object_details.value)
        print("Valeur de l'objet :", object_details.description)
    else:
        print("Objet non trouvé ou erreur de requête.")

asyncio.run(main())