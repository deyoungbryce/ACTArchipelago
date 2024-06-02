from worlds.AutoWorld import WebWorld, World
from BaseClasses import Item, Location, ItemClassification, Region

from .Items import item_name_to_id, item_table, item_name_groups, filler_items
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
    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id

    def create_item(self, item: str) -> ACTItem:
        return ACTItem(item, item_table[item].classification, self.item_name_to_id[item], self.player)

    def create_event(self, event: str) -> ACTItem:
        return ACTItem(event, ItemClassification.progression, None, self.player)

    def create_items(self) -> None:
        exclude = [item for item in self.multiworld.precollected_items[self.player]]
        item_pool = []

        for item_name, item_data in item_table.items():
            for _ in range(item_data.quantity_in_item_pool):
                item_pool.append(self.create_item(item_name))

        self.multiworld.itempool += item_pool

        filler_amount = len(self.multiworld.get_unfilled_locations(self.player)) - len(item_pool)
        for _ in range(filler_amount):
            self.multiworld.itempool += self.create_item(self.get_filler_item_name())

    def create_regions(self):
        player = self.player
        multiworld = self.multiworld

        menu = Region("Menu", player, multiworld)
        multiworld.regions.append(menu)

    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_items)
