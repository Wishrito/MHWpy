from mhw_api_wrapper.mhw_wrapper import MHWDBWrapper
from wrapper.mhw_api_wrapper.details import MotionDetails

async def get_all_motion(wrapper: MHWDBWrapper):
    endpoint = "/motion-values"
    return wrapper.make_request(endpoint)

async def get_motion_by_id(wrapper: MHWDBWrapper, motion_id: int):
    endpoint = f"/motion-values/{motion_id}"
    motion_data = wrapper.make_request(endpoint)
    if motion_data:
        return MotionDetails(motion_data)
    return None