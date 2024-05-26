from typing import Dict
from ..AutoWorld import WebWorld, World
from ...BaseClasses import Item, Location, ItemClassification, Region

from .Items import item_table, item_name_groups, item_ids, filler_items
from .Locations import location_table, location_name_groups, location_ids
from .Regions import ACT_regions
from .Rules import set_location_rules, set_region_rules
from .Options import ACTGameOptions


class ACTWeb(WebWorld):
    theme = "ocean"
    game = "Another Crab's Treasure"

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
    item_name_groups = item_name_groups
    location_name_groups = location_name_groups

    def create_item(self, item: str) -> ACTItem:
        item_data = item_table[item]
        return ACTItem(item, item_data.classification, self.item_ids[item], self.player)

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

        for region_name in ACT_regions:
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)
        
        for location_name, location_id in location_ids.items():
            region = self.multiworld.get_region(location_table[location_name].region, self.player)
            location = ACTLocation(self.player, location_name, location_id, region)
            region.locations.append(location)

        victory_region = self.multiworld.get_region("Fort Slacktide - After Destruction", self.player)
        victory_location = ACTLocation(self.player, "Royal Wave Adaptation (Fort Slacktide - Defeat Magista)", None, victory_region)

    def set_rules(self) -> None:
        set_region_rules(self)
        set_location_rules(self)

    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_items)