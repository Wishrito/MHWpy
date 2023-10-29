from mhw_api_wrapper.mhw_wrapper import MHWDBWrapper
from wrapper.mhw_api_wrapper.details import WeaponDetails

async def get_all_weapons(wrapper: MHWDBWrapper):
    endpoint = "/weapons"
    return wrapper.make_request(endpoint)

async def get_weapon_by_id(wrapper: MHWDBWrapper, weapon_id: int):
    endpoint = f"/weapons/{weapon_id}"
    weapon_data = wrapper.make_request(endpoint)
    if weapon_data:
        return WeaponDetails(weapon_data)
    return None