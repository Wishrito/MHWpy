from mhw_api_wrapper.mhw_wrapper import MHWDBWrapper
from wrapper.mhw_api_wrapper.details import ArmorDetails, ArmorSetDetails

# Armor only
async def get_all_armors(wrapper: MHWDBWrapper):
    endpoint = f"/armor/"
    return wrapper.make_request(endpoint)

async def get_armor_by_id(wrapper: MHWDBWrapper, armor_id: int):
    endpoint = f"/armor/{armor_id}"
    armor_data = wrapper.make_request(endpoint)
    if armor_data:
        return ArmorDetails(armor_data)
    return None

# Armor set
async def get_all_armor_set(wrapper: MHWDBWrapper):
    endpoint = f"/armor/sets/"
    return wrapper.make_request(endpoint)

async def get_armor_set_by_id(wrapper: MHWDBWrapper, armor_set_id: int):
    endpoint = f"/armor/sets/{armor_set_id}"
    armor_set_data = wrapper.make_request(endpoint)
    if armor_set_data:
        return ArmorSetDetails(armor_set_data)
    return None