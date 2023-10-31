from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Dict
from mhw_api_wrapper.mhw_wrapper import MHWDBWrapper
from mhw_api_wrapper.details import ElementDetails
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

@dataclass(order=True)
class AssetDetails:
    imageMale: str
    imageFemale: str
    
    def __repr__(self):
        return f"AssetDetails(imageMale={self.imageMale}, imageFemale={self.imageFemale})"

@dataclass(order=True)
class SoftArmorDetails:
    id: int
    slug: str
    name: str
    type: str
    rank: int
    rarity: int
    defense: dict[int, int]
    resistances: dict[ElementDetails, ElementDetails]
    slots: List[dict]
    attributes: dict
    skills: List
    assets: List[AssetDetails]

    def __repr__(self):
        return f"SoftArmorDetails(id={self.id}, name={self.name}, type={self.type}, rarity={self.rarity}, slug={self.slug})"

@dataclass(order=True)
class ArmorSetDetails:
    id: int
    name: str
    rank: str
    pieces: List[SoftArmorDetails]
    bonus: str
    attributes: Dict
    skills: List
    assets: AssetDetails

    def __repr__(self):
        return f"ArmorSetDetails(id={self.id}, name={self.name}, rank={self.rank}, bonus={self.bonus}, skills={self.skills})"


@dataclass(order=True)
class ArmorDetails:
    id: int
    slug: str
    name: str
    type: str
    rank: int
    rarity: int
    defense: dict
    resistances: ElementDetails  # Utilisez la classe ResistanceDetails pour les résistances
    slots: List[dict]
    attributes: dict
    skills: List
    armorSet: ArmorSetDetails
    assets: AssetDetails
    crafting: List[dict]
    
    def __repr__(self):
        return (
            f"ArmorDetails(id={self.id}, name={self.name}, type={self.type}, "
            f"rarity={self.rarity}, slug={self.slug})"
        )

# Armor only
async def get_all_armors(wrapper: MHWDBWrapper):
    endpoint = f"/armor/"
    return wrapper.make_request(endpoint)

async def get_armor_by_id(wrapper: MHWDBWrapper, armor_id: int):
    """
    Function to retrieve details about a specified armor piece from the MHWpy API.

    Parameters
    ----------
    wrapper: MHWDBWrapper
        An instance of the MHWDBWrapper.
    item_id: int
        The unique ID of the item.

    Returns
    -------
    ArmorDetails
        Details of the specified Armor piece, or None if the Armor piece is not found.
    """
    endpoint = f"/armor/{armor_id}"
    armor_data = wrapper.make_request(endpoint)
    if armor_data:
        armor_details = ArmorDetails(
            id=armor_data.get("id"),
            slug=armor_data.get("slug"),
            name=armor_data.get("name"),
            type=armor_data.get("value"),
            rank=armor_data.get("rank"),
            rarity=armor_data.get("rarity"),
            defense=armor_data.get("defense"),
            resistances=armor_data.get("resistances"),
            slots=armor_data.get("slots"),
            attributes=armor_data.get("attributes"),
            skills=armor_data.get("skills"),
            armorSet=armor_data.get("armorSet"),
            assets=armor_data.get("assets"),
            crafting=armor_data.get("crafting")
        )
        return armor_details
    return None

# Armor set
async def get_all_armor_set(wrapper: MHWDBWrapper):
    endpoint = f"/armor/sets/"
    return wrapper.make_request(endpoint)

async def get_armor_set_by_id(wrapper: MHWDBWrapper, armor_set_id: int):
    endpoint = f"/armor/sets/{armor_set_id}"
    armor_set_data = wrapper.make_request(endpoint)
    if armor_set_data:
        armor_details = ArmorSetDetails(
            id=armor_set_data.get("id"),
            name=armor_set_data.get("name"),
            rank=armor_set_data.get("rank"),
            pieces=armor_set_data.get("pieces"),
            bonus=armor_set_data.get("bonus"),
            attributes=armor_set_data.get("attributes"),
            skills=armor_set_data.get("skills"),
            assets=armor_set_data.get("assets")
        )
        return armor_details
    return None