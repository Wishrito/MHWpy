from mhw_api_wrapper.mhw_wrapper import MHWDBWrapper
from wrapper.mhw_api_wrapper.details import LocationDetails  # Importez la nouvelle classe ItemDetails

async def get_all_locations(wrapper: MHWDBWrapper):
    endpoint = "/locations"
    return wrapper.make_request(endpoint)

async def get_location_by_id(wrapper: MHWDBWrapper, location_id: int):
    endpoint = f"/locations/{location_id}"
    location_data = wrapper.make_request(endpoint)
    if location_data:
        return LocationDetails(location_data)
    return None