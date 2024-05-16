from typing import List, TypedDict

from ...BaseClasses import Item, ItemClassification

class ItemDict(TypedDict):
    name: str
    id: int
    count: int
    classification: ItemClassification

base_id = 0

item_table:  List[ItemDict] = [
    
    {"name": "Fork", "id": base_id + 1, "count": 1, "classification": ItemClassification.progression},
    {"name": "Map Piece", "id": base_id + 2, "count": 3, "classification": ItemClassification.progression}

]