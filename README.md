
# MHWpy API Wrapper

This is a Python wrapper for the MHWpy API, which provides information about Monster Hunter World (MHW) game data.

## Installation

You can install the MHWpy API wrapper by downloading ``MonsterHunterWorldPy-VERSION.tar.gz``, and using pip:

```bash
pip install MonsterHunterWorldPy-VERSION.tar.gz
```

## Usage

### Initializing the Wrapper

First, you need to create an instance of the `MHWDBWrapper`:

```python
from mhw_api_wrapper.mhw_wrapper import MHWDBWrapper

mhw_api = MHWDBWrapper()
```

### Getting Monster Details

You can use the `get_monster_by_id` function to get details about a specific monster:

```python
from mhw_api_wrapper.mhw_wrapper import MHWDBWrapper
from mhw_api_wrapper import monsters
import asyncio

async def get_monster_details():
    monster_id = 1
    monster_details = await mhw_api.get_monster_by_id(monster_id)
    
    if monster_details:
        print("Monster Name:", monster_details.name)
        print("Type:", monster_details.type)
        print("Description:", monster_details.description)

asyncio.run(get_monster_details())
```

### Getting Armor Details

You can use the `get_armor_by_id` function to get details about a specific armor:

```python
from mhw_api_wrapper.mhw_wrapper import MHWDBWrapper
from mhw_api_wrapper import armors
import asyncio

async def get_armor_details():
    armor_id = 50
    armor_details = await mhw_api.get_armor_by_id(armor_id)
    
    if armor_details:
        print("Armor Name:", armor_details.name)
        print("Rank:", armor_details.rank)
        print("Rarity:", armor_details.rarity)

asyncio.run(get_armor_details())
```

### Getting Item Details

You can use the `get_item_by_id` function to get details about a specific item:

```python
from mhw_api_wrapper.mhw_wrapper import MHWDBWrapper
from mhw_api_wrapper import items
import asyncio

async def get_item_details():
    item_id = 67
    item_details = await mhw_api.get_item_by_id(item_id)
    
    if item_details:
        print("Item Name:", item_details.name)
        print("Description:", item_details.description)
        print("Rarity:", item_details.rarity)

asyncio.run(get_item_details())
```

## Contribution

Feel free to contribute to this project by opening issues or submitting pull requests.

## License

This project is licensed under the MIT License.
