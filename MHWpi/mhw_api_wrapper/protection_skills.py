from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass(order=True)
class SkillDetails:
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
    slug : str
    name: str
    description: str
    rank: List[dict]

    def __repr__(self):
        return (
            f"Protection_skillsDetails(id={self.id}, name={self.name}"
            f"description={self.description})"
        )