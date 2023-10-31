"""
The MIT License (MIT)

Copyright (c) 2023-present Wishrito

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from mhw_api_wrapper.mhw_wrapper import MHWDBWrapper
from mhw_api_wrapper.details import MonsterDetails

async def get_all_monsters(wrapper: MHWDBWrapper):
    """
    Class representing some details about all monsters from the MHWpy API.

    Attributes
    ----------
    id: `int`
        The id of the monster.
    name: `str`
        The name of the monster.
    type: `str`
        The type of the monster.
    species: `str`
        The species of the monster.
    description: `str`
        The description of the monster.
    elements: `List[str]`
        The elements of the monster.
    ailments: `List[str]`
        The ailments of the monster.
    locations: `List[str]`
        The locations where you can found this monster.
    resistances: `List[str]`
        The resistances of the monster.
    weaknesses: `List[dict]`
        The weaknesses of the monster.
    rewards: `List[dict]`
    """
    endpoint = "/monsters"
    monster_data = wrapper.make_request(endpoint)
    if monster_data:
        monster_list = []
        for data in monster_data:
            monster = MonsterDetails(
                id=data.get("id"),
                name=data.get("name"),
                type=data.get("type"),
                species=data.get("species"),
                description=data.get("description"),
                elements=data.get("elements"),
                ailments=data.get("ailments"),
                locations=data.get("locations"),
                resistances=data.get("resistances"),
                weaknesses=data.get("weaknesses"),
                rewards=data.get("rewards")
            )
            monster_list.append(monster)
        return monster_list
    return []

async def get_monster_by_id(wrapper: MHWDBWrapper, monster_id: int):
    """
    Class representing some details about a specific Monster from the MHWpy API.

    Attributes
    ----------
    id: `int`
        The id of the monster.
    name: `str`
        The name of the monster.
    type: `str`
        The type of the monster.
    species: `str`
        The species of the monster.
    description: `str`
        The description of the monster.
    elements: `List[str]`
        The elements of the monster.
    ailments: `List[str]`
        The ailments of the monster.
    locations: `List[str]`
        The locations where you can found this monster.
    resistances: `List[str]`
        The resistances of the monster.
    weaknesses: `List[dict]`
        The weaknesses of the monster.
    rewards: `List[dict]`
    """
    endpoint = f"/monsters/{monster_id}"
    monster_data = wrapper.make_request(endpoint)
    if monster_data:
        return MonsterDetails(
            id=monster_data.get("id"),
            name=monster_data.get("name"),
            type=monster_data.get("type"),
            species=monster_data.get("species"),
            description=monster_data.get("description"),
            elements=monster_data.get("elements"),
            ailments=monster_data.get("ailments"),
            locations=monster_data.get("locations"),
            resistances=monster_data.get("resistances"),
            weaknesses=monster_data.get("weaknesses"),
            rewards=monster_data.get("rewards")
        )
    return None
