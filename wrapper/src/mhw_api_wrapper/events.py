from mhw_api_wrapper.mhw_wrapper import MHWDBWrapper
from wrapper.mhw_api_wrapper.details import EventDetails

async def get_all_charm(wrapper: MHWDBWrapper):
    endpoint = "/events"
    return wrapper.make_request(endpoint)

async def get_charm_by_id(wrapper: MHWDBWrapper, event_id: int):
    endpoint = f"/events/{event_id}"
    event_data = wrapper.make_request(endpoint)
    if event_data:
        return EventDetails(event_data)
    return None