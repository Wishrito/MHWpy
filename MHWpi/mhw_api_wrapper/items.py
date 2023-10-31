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
from mhw_api_wrapper.details import ItemDetails

async def get_all_item(wrapper: MHWDBWrapper):
    """
    Function representing some Item details about all Items from the MHWpy API.

    Attributes
    ----------
    id: `int`
        The id of the item.
    name: `str`
        The name of the item.
    description: `str`
        The description of the item.
    rarity: `int`
        The rarity of the item.
    carryLimit: `int`
        The carrying limit of the item.
    value: `int`
        The id of the item.
    """
    endpoint = "/items"
    return wrapper.make_request(endpoint)

async def get_item_by_id(wrapper: MHWDBWrapper, item_id: int):
    """
    Function to retrieve details about a specified item from the MHWpy API.

    Parameters
    ----------
    wrapper: MHWDBWrapper
        An instance of the MHWDBWrapper.
    item_id: int
        The unique ID of the item.

    Returns
    -------
    ItemDetails
        Details of the specified item, or None if the item is not found.
    """
    endpoint = f"/items/{item_id}"
    item_data = wrapper.make_request(endpoint)
    if item_data:
        item_details = ItemDetails(
            id=item_data.get("id"),
            name=item_data.get("name"),
            description=item_data.get("description"),
            rarity=item_data.get("rarity"),
            carryLimit=item_data.get("carryLimit"),
            value=item_data.get("value")
        )
        return item_details
    return None