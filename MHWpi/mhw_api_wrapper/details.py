from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Dict
"""
details module for the MHWpy API.
"""

@dataclass(order=True)
class AilmentDetails:
    """
    Class representing ailment details from the MHWpy API.

    Attributes
    ----------
    id: int
        The id of the ailment.
    name: str
        The name of the ailment.
    description: str
        The description of the ailment.
    elements: List[str]
        A list of elements associated with the ailment.
    ailments: List[str]
        A list of ailments associated with the ailment.
    locations: List[dict]
        A list of locations where the ailment is found. The annotation should be adapted to the actual data.
    resistances: List[str]
        A list of resistances associated with the ailment.
    weaknesses: List[dict]
        A list of weaknesses of the ailment. The annotation should be adapted to the actual data.
    rewards: List[dict]
        A list of rewards for the ailment. The annotation should be adapted to the actual data.
    """
    id: int
    name: str
    description: str
    recovery_actions: List[str]
    recovery_item: List[dict]
    protection_items: List[dict]
    protection_skills: AilmentDetails

    def __post_init__(self):
        for data in self.protection_items:
            data["id"] = data["id"] if "id" in data else None
            data["name"] = data["name"] if "name" in data else None
            data["description"] = data["description"] if "description" in data else None
            
        for data in self.recovery_item:
            data["id"] = data["id"] if "id" in data else None
            data["name"] = data["name"] if "name" in data else None
            data["description"] = data["description"] if "description" in data else None
            

    def __repr__(self):
        return (
            f"MonsterDetails(id={self.id}, name={self.name}"
            f"description={self.description})"
        )

@dataclass(order=True)
class ItemDetails:
    id: int
    name: str
    description: str
    rarity: int
    carryLimit: int
    value: int

    def __repr__(self):
        return (
            f"ItemDetails(id={self.id}, name={self.name}, description={self.description}, "
            f"rarity={self.rarity}, carryLimit={self.carryLimit}, value={self.value})"
        )

@dataclass(order=True)
class MonsterDetails:
    id: int
    name: str
    type: str
    species: str
    description: str
    elements: List[str]
    ailments: List[str]
    locations: List[dict]  # Vous devrez adapter cette annotation de type aux données réelles
    resistances: List[str]
    weaknesses: List[dict]  # Vous devrez adapter cette annotation de type aux données réelles
    rewards: List[dict]  # Vous devrez adapter cette annotation de type aux données réelles

    def __post_init__(self):
        for data in self.locations:
            data["element"] = data["element"] if "element" in data else None
            data["condition"] = data["condition"] if "condition" in data else None

        for data in self.rewards:
            data["id"] = data["id"] if "id" in data else None
            data["item"] = data["item"] if "item" in data else None
            data["chance"] = data["chance"] if "chance" in data else None

    def __repr__(self):
        return (
            f"MonsterDetails(id={self.id}, name={self.name}, type={self.type}, "
            f"species={self.species}, description={self.description})"
        )

class LocationDetails:
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")
        self.zoneCount = data.get("zoneCount")
        self.camps = data.get("camps")

        # Si vous souhaitez accéder aux propriétés des camps, vous pouvez le faire comme suit.
        if self.camps:
            # Accédez au premier camp
            first_camp = self.camps[0]
            self.camp_id = first_camp.get("id")
            self.camp_name = first_camp.get("name")
            self.camp_zone = first_camp.get("zone")

class SkillDetails:
    def __init__(self, data):
        self.id = data.get("id")
        self.slug = data.get("slug")
        self.name = data.get("name")
        self.description = data.get("description")
        self.ranks = data.get("ranks")

        # Si vous souhaitez accéder aux propriétés des rangs, vous pouvez le faire comme suit.
        if self.ranks:
            # Accédez au premier rang
            first_rank = self.ranks[0]
            self.rank_id = first_rank.get("id")
            self.rank_slug = first_rank.get("slug")
            self.rank_skill = first_rank.get("skill")
            self.rank_level = first_rank.get("level")
            self.rank_description = first_rank.get("description")
            self.rank_modifiers = first_rank.get("modifiers")

class WeaponDetails:
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")
        self.type = data.get("type")
        self.rarity = data.get("rarity")
        self.attack = data.get("attack")
        self.elderseal = data.get("elderseal")
        self.attributes = data.get("attributes")
        self.damageType = data.get("damageType")
        self.durability = data.get("durability")
        self.slots = data.get("slots")
        self.elements = data.get("elements")
        self.crafting = data.get("crafting")
        self.assets = data.get("assets")

class MotionDetails:
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")
        self.weaponType = data.get("weaponType")
        self.damageType = data.get("damageType")
        self.stun = data.get("stun")
        self.exhaust = data.get("exhaust")
        self.values = data.get("values")

class CharmDetails:
    def __init__(self, data):
        self.id = data.get("id")
        self.slug = data.get("slug")
        self.name = data.get("name")
        self.ranks = data.get("ranks")

        # Si vous souhaitez accéder aux propriétés des rangs, vous pouvez le faire comme suit.
        if self.ranks:
            # Accédez au premier rang
            first_rank = self.ranks[0]
            self.rank_level = first_rank.get("level")
            self.rank_rarity = first_rank.get("rarity")
            self.rank_skills = first_rank.get("skills")
            self.rank_crafting = first_rank.get("crafting")

class DecorationDetails:
    def __init__(self, data):
        self.id = data.get("id")
        self.slug = data.get("slug")
        self.name = data.get("name")
        self.rarity = data.get("rarity")
        self.skills = data.get("skills")
        self.slot = data.get("slot")

        # Si vous souhaitez accéder aux propriétés des compétences, vous pouvez le faire comme suit.
        if self.skills:
            # Accédez à la première compétence
            first_skill = self.skills[0]
            self.skill_id = first_skill.get("id")
            self.skill_slug = first_skill.get("slug")
            self.skill_description = first_skill.get("description")
            self.skill_level = first_skill.get("level")
            self.skill_skill = first_skill.get("skill")
            self.skill_skillName = first_skill.get("skillName")
            self.skill_modifiers = first_skill.get("modifiers")

class EventDetails:
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")
        self.platform = data.get("platform")
        self.exclusive = data.get("exclusive")
        self.type = data.get("type")
        self.expansion = data.get("expansion")
        self.description = data.get("description")
        self.requirements = data.get("requirements")
        self.questRank = data.get("questRank")
        self.successConditions = data.get("successConditions")
        self.startTimestamp = data.get("startTimestamp")
        self.endTimestamp = data.get("endTimestamp")
        self.location = data.get("location")
