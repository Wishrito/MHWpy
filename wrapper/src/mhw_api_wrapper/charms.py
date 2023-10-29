from mhw_api_wrapper.mhw_wrapper import MHWDBWrapper
from wrapper.mhw_api_wrapper.details import CharmDetails

async def get_all_charm(wrapper: MHWDBWrapper):
    endpoint = "/charm"
    return wrapper.make_request(endpoint)

async def get_charm_by_id(wrapper: MHWDBWrapper, charm_id: int):
    endpoint = f"/charm/{charm_id}"
    charm_data = wrapper.make_request(endpoint)
    if charm_data:
        return CharmDetails(charm_data)
    return None
