from mhw_api_wrapper.mhw_wrapper import MHWDBWrapper
from wrapper.mhw_api_wrapper.details import ItemDetails

async def get_all_item(wrapper: MHWDBWrapper):
    endpoint = "/items"
    return wrapper.make_request(endpoint)

async def get_item_by_id(wrapper: MHWDBWrapper, item_id: int):
    endpoint = f"/items/{item_id}"
    item_data = wrapper.make_request(endpoint)
    if item_data:
        return ItemDetails(item_data)
    return None
