from mhw_api_wrapper.mhw_wrapper import MHWDBWrapper

async def get_all_monsters(wrapper: MHWDBWrapper):
    endpoint = "/monsters"
    return wrapper.make_request(endpoint)

async def get_monster_by_id(wrapper: MHWDBWrapper, monster_id: int):
    endpoint = f"/monsters/{monster_id}"
    return wrapper.make_request(endpoint)