from typing import Dict, List
from worlds.AutoWorld import WebWorld, World
from BaseClasses import Item, Location, ItemClassification, Region, MultiWorld

from .Items import item_table, item_name_groups, item_name_to_id, filler_items, ACTItem
from .Locations import location_table, location_name_groups, location_name_to_id, ACTLocation
from .Regions import ACT_regions
from .Rules import set_location_rules, set_region_rules
from .Options import ACTGameOptions


class ACTWeb(WebWorld):
    theme = "ocean"
    game = "Another Crabs Treasure"

class ACTWorld(World):
    """
    Another Crab's Treasure is an underwater souls-like with a charming art style and a quirky sense of humor.
    """
    game: str = "Another Crabs Treasure"
    web = ACTWeb()

    options_dataclass = ACTGameOptions
    options: ACTGameOptions
    item_name_groups = item_name_groups
    location_name_groups = location_name_groups

    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id

    slot_data_items = List[ACTItem]

    def create_item(self, name: str) -> ACTItem:
        item_data = item_table[name]
        return ACTItem(name, item_data.classification, self.item_name_to_id[name], self.player)

    def create_event(self, event: str) -> ACTItem:
        return ACTItem(event, True, None, self.player)

    def create_items(self) -> None:
        ACT_items: List[ACTItem] = []
        self.slot_data_items = []

        items_to_create: Dict[str, int] = {item: data.quantity_in_item_pool for item, data in item_table.items()}

        for item, quantity in items_to_create.items():
            for i in range(quantity):
                ACT_item: ACTItem = self.create_item(item)
                ACT_items.append(ACT_item)

        self.multiworld.itempool += ACT_items

        '''exclude = [item for item in self.multiworld.precollected_items[self.player]]

        for item in map(self.create_item, ACTItem):
            if item in exclude:
                exclude.remove(item)
                self.multiworld.itempool.append(self.create_item("nothing"))
            else:
                self.multiworld.itempool.append(item)
            
        junk = 0
        self.multiworld.itempool += [self.create_item("nothing") for _ in range(junk)]'''

    def create_regions(self):
        player = self.player
        multiworld = self.multiworld

        menu = Region("Menu", player, multiworld)
        multiworld.regions.append(menu)

        for region_name in ACT_regions:
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        for region_name, exits in ACT_regions.items():
            region = self.multiworld.get_region(region_name, self.player)
            region.add_exits(exits)
        
        for location_name, location_id in location_name_to_id.items():
            region = self.multiworld.get_region(location_table[location_name].region, self.player)
            location = ACTLocation(self.player, location_name, location_id, region)
            region.locations.append(location)

        victory_region = self.multiworld.get_region("Fort Slacktide - After Destruction", self.player)
        victory_location = ACTLocation(self.player, "Royal Wave Adaptation (Fort Slacktide - Defeat Magista)", None, victory_region)
        victory_location.place_locked_item(ACTItem("Victory", ItemClassification.progression, None, self.player))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
        victory_region.locations.append(victory_location)

    def set_rules(self) -> None:
        set_region_rules(self)
        set_location_rules(self)

    # to be used later if we add locations that don't already have items assigned to them
    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_items)