from mhw_api_wrapper.mhw_wrapper import MHWDBWrapper
from wrapper.mhw_api_wrapper.details import AilmentDetails

# Armor only
async def get_all_armors(wrapper: MHWDBWrapper):
    endpoint = f"/ailment"
    return wrapper.make_request(endpoint)

async def get_armor_by_id(wrapper: MHWDBWrapper, ailment_id: int):
    endpoint = f"/ailment/{ailment_id}"
    ailment_data = wrapper.make_request(endpoint)
    if ailment_data:
        return AilmentDetails(ailment_data)
    return None