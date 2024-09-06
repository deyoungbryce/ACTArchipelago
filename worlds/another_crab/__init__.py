from typing import Dict, List
from worlds.AutoWorld import WebWorld, World
from BaseClasses import Region, ItemClassification

from .items import item_table, item_name_groups, item_name_to_id, filler_items, costume_items, ACTItem
from .locations import location_table, location_name_groups, location_name_to_id, ACTLocation
from .regions import ACT_regions
from .rules import set_location_rules, set_region_rules
from .options import ACTGameOptions
from .names import location_names as lname, item_names as iname, region_names as rname


class ACTWeb(WebWorld):
    theme: str = "ocean"
    game: str = "Another Crab's Treasure"

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

    #slot_data_items = List[ACTItem]

    def create_item(self, name: str) -> ACTItem:
        item_data = item_table[name]
        return ACTItem(name, item_data.classification, self.item_name_to_id[name], self.player)

    # not actually used rn
    def create_event(self, event: str) -> ACTItem:
        return ACTItem(event, True, None, self.player)

    def create_items(self) -> None:
        ACT_items: List[ACTItem] = []
        costume_list = costume_items
        #self.slot_data_items = []

        items_to_create: Dict[str, int] = {item: data.quantity_in_item_pool for item, data in item_table.items()}

        if self.options.forkLocation:
            fork = self.create_item(iname.fork)
            if self.options.forkLocation == "vanilla_location":
                self.multiworld.get_location(lname.fork_pickup, self.player).place_locked_item(fork)
            items_to_create[iname.fork] = 0

        if self.options.shelleportLocation:
            shelleport = self.create_item(iname.shelleport)
            if self.options.shelleportLocation == "starting_items":
                self.multiworld.push_precollected(shelleport)
            elif self.options.shelleportLocation == "vanilla_location":
                self.multiworld.get_location(lname.shelleport_skill, self.player).place_locked_item(shelleport)
            items_to_create[iname.shelleport] = 0

        if self.options.fishinglinelocation:
            fishing_line = self.create_item(iname.fishing_line)
            if self.options.fishinglinelocation == "vanilla_location":
                self.multiworld.get_location(lname.fishing_line, self.player).place_locked_item(fishing_line)
            items_to_create[iname.fishing_line] = 0

        if self.options.removeCostumes:
            items_to_create[costume_list] = 0

        for item, quantity in items_to_create.items():
            for i in range(quantity):
                ACT_item: ACTItem = self.create_item(item)
                ACT_items.append(ACT_item)

        available_filler: List[str] = [filler for filler in items_to_create if items_to_create[filler] > 0 and item_table[filler].classification == ItemClassification.filler]

        self.multiworld.itempool += ACT_items

    def create_regions(self):

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

        self.multiworld.completion_condition[self.player] = \
            lambda state: state.can_reach(spot = lname.royal_wave_reward, resolution_hint="Location", player = self.player)

    def set_rules(self) -> None:
        set_region_rules(self)
        set_location_rules(self)

    # can probably be removed?
    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_items)