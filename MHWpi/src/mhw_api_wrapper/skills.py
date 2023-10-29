from mhw_api_wrapper.mhw_wrapper import MHWDBWrapper
from mhw_api_wrapper.details import SkillDetails

async def get_all_skills(wrapper: MHWDBWrapper):
    endpoint = "/skills"
    return wrapper.make_request(endpoint)

async def get_skill_by_id(wrapper: MHWDBWrapper, skill_id: int):
    endpoint = f"/skills/{skill_id}"
    skill_data = wrapper.make_request(endpoint)
    if skill_data:
        return SkillDetails(skill_data)
    return None