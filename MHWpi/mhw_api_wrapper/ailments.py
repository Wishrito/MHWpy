from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Dict
from mhw_api_wrapper.mhw_wrapper import MHWDBWrapper
from mhw_api_wrapper.details import AilmentDetails
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


async def get_all_ailment(wrapper: MHWDBWrapper):
    """
    Function representing some Ailments details about all Items from the MHWpy API.

    Attributes
    ----------
    id: `int`
        The id of the Ailment.
    name: `str`
        The name of the Ailment.
    description: `str`
        The description of the Ailment.
    rarity: `int`
        The rarity of the item.
    carryLimit: `int`
        The carrying limit of the item.
    value: `int`
        The id of the item.
    """
    endpoint = "/items"
    return wrapper.make_request(endpoint)

async def get_ailment_by_id(wrapper: MHWDBWrapper, ailment_id: int):
    """
    Function to retrieve details about a specified ailment from the MHWpy API.

    Parameters
    ----------
    wrapper: MHWDBWrapper
        An instance of the MHWDBWrapper.
    ailment_id: int
        The unique ID of the item.

    Returns
    -------
    AilmentDetails
        Details of the specified Ailment, or None if the Ailment is not found.
    """
    endpoint = f"/items/{ailment_id}"
    ailment_data = wrapper.make_request(endpoint)
    if ailment_data:
        ailment_details = AilmentDetails(
            id=ailment_data.get("id"),
            name=ailment_data.get("name"),
            description=ailment_data.get("description"),
            recovery_actions=ailment_data.get("recovery_actions"),
            recovery_item=ailment_data.get("recovery_items"),
            protection_items=ailment_data.get("protection_items"),
            protection_skills=ailment_data.get("protection_skills")
        )
        return ailment_details
    return None