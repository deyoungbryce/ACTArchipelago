from itertools import groupby
from typing import Dict, List, Set, NamedTuple
from BaseClasses import ItemClassification
from .names import item_names as iname

item_base_id = 483021700

class ACTItemData(NamedTuple):
    classification: ItemClassification
    quantity_in_item_pool: int
    item_group: str = ""


item_table: Dict[str, ACTItemData] = {
    # progression
    iname.fork: ACTItemData(ItemClassification.progression, 1, "Progression"),

    #upgrade
    iname.bloodstar_limb: ACTItemData(ItemClassification.useful, 25 , "Upgrades"),
    iname.heartkelp_sprout: ACTItemData(ItemClassification.useful, 7, "Upgrades"),
    iname.old_whorl: ACTItemData(ItemClassification.useful, 11, "Upgrades"),
    iname.stainless_relic: ACTItemData(ItemClassification.useful, 15, "Upgrades"),
    iname.tackle_pouch: ACTItemData(ItemClassification.useful, 1, "Upgrades") # setting quantity to 1 for now because i don't know how many there are in the game
}