
# MHWpy API Wrapper

This is a Python wrapper for the MHWpy API, which provides information about Monster Hunter World (MHW) game data.

## Installation

You can install the MHWpy API wrapper using pip:

```bash
pip install mhwpy-wrapper
```

## Usage

### Initializing the Wrapper

First, you need to create an instance of the `MHWDBWrapper`:

```python
from mhwpy_wrapper import MHWDBWrapper

mhw_api = MHWDBWrapper(base_url="https://api.mhwpy.com")
```

### Getting Monster Details

You can use the `get_monster_by_id` function to get details about a specific monster:

```python
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

```

This example README.md provides a simple introduction to the API wrapper, installation instructions, usage examples for various functions, information on how to contribute, and the license. You can customize it to fit your project's needs.
```
