from typing import Dict
from ..AutoWorld import WebWorld, World
from ...BaseClasses import Item, Location, ItemClassification, Region

from .Items import item_name_to_id, item_table, item_name_groups
from .Locations import location_table, location_name_groups, location_name_to_id
from .Options import ACTGameOptions


class ACTWeb(WebWorld):
    theme = "ocean"

class ACTItem(Item):
    game = "Another Crab's Treasure"

class ACTLocation(Location):
    game = "Another Crab's Treasure"

class ACTWorld(World):
    """
    Another Crab's Treasure is an underwater souls-like with a charming art style and a quirky sense of humor.
    """
    game = "Another Crab's Treasure"
    web = ACTWeb()
    options_dataclass = ACTGameOptions
    options: ACTGameOptions

    def create_item(self, item: str) -> ACTItem:
        classification = ItemClassification.progression if item.classification == ItemClassification.progression else ItemClassification.filler
        return ACTItem(item, classification, self.item_name_to_id[item], self.player)

    def create_event(self, event: str) -> ACTItem:
        return ACTItem(event, True, None, self.player)

    def create_items(self) -> None:
        exclude = [item for item in self.multiworld.precollected_items[self.player]]

        for item in map(self.create_item, ACTItem):
            if item in exclude:
                exclude.remove(item)
                self.multiworld.itempool.append(self.create_item("nothing"))
            else:
                self.multiworld.itempool.append(item)
            
        junk = 0
        self.multiworld.itempool += [self.create_item("nothing") for _ in range(junk)]

    def create_regions(self):
        player = self.player
        multiworld = self.multiworld

        menu = Region("Menu", player, multiworld)
        multiworld.regions.append(menu)