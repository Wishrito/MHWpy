from mhw_api_wrapper.mhw_wrapper import MHWDBWrapper
from wrapper.mhw_api_wrapper.details import DecorationDetails

async def get_all_charm(wrapper: MHWDBWrapper):
    endpoint = "/decorations"
    return wrapper.make_request(endpoint)

async def get_charm_by_id(wrapper: MHWDBWrapper, decoration_id: int):
    endpoint = f"/decorations/{decoration_id}"
    decoration_data = wrapper.make_request(endpoint)
    if decoration_data:
        return DecorationDetails(decoration_data)
    return None