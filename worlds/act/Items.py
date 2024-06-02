from itertools import groupby
from typing import Dict, List, Set, NamedTuple
from BaseClasses import ItemClassification
from .names import item_names as iname

item_base_id = 483021700


class ACTItemData(NamedTuple):
    classification: ItemClassification
    quantity_in_item_pool: int
    item_group: str = ""


# a lot of quantities here will need to be adjusted later
item_table: Dict[str, ACTItemData] = {
    # progression
    iname.fork: ACTItemData(ItemClassification.progression, 1, "Progression"), 
    iname.heartkelp_pod: ACTItemData(ItemClassification.progression, 1, "Progression"),  # throwing this into the progression items because the average player will definitely need heals to beat the game
    iname.fishing_line: ACTItemData(ItemClassification.progression, 1, "Progression"),
    iname.pristine_pearl: ACTItemData(ItemClassification.progression, 1, "Progression"),
    iname.map_piece_fv: ACTItemData(ItemClassification.progression, 1, "Progression"),
    iname.map_piece_heikea: ACTItemData(ItemClassification.progression, 1, "Progression"),
    iname.map_piece_pagurus: ACTItemData(ItemClassification.progression, 1, "Progression"),

    # upgrade
    iname.bloodstar_limb: ACTItemData(ItemClassification.useful, 25, "Upgrades"),
    iname.heartkelp_sprout: ACTItemData(ItemClassification.useful, 7, "Upgrades"),
    iname.old_whorl: ACTItemData(ItemClassification.useful, 11, "Upgrades"),
    iname.stainless_relic: ACTItemData(ItemClassification.useful, 15, "Upgrades"),
    iname.tackle_pouch: ACTItemData(ItemClassification.useful, 1, "Upgrades"),

    # stowaways
    iname.siphonophore: ACTItemData(ItemClassification.useful, 1, "Stowaways"),
    iname.seastar: ACTItemData(ItemClassification.useful, 1, "Stowaways"),
    iname.sponge: ACTItemData(ItemClassification.useful, 1, "Stowaways"),
    iname.another_crab: ACTItemData(ItemClassification.useful, 1, "Stowaways"),
    iname.sand_dollar: ACTItemData(ItemClassification.useful, 1, "Stowaways"),
    iname.limpet: ACTItemData(ItemClassification.useful, 1, "Stowaways"),
    iname.barnacle: ACTItemData(ItemClassification.useful, 1, "Stowaways"),
    iname.mussel: ACTItemData(ItemClassification.useful, 1, "Stowaways"),
    iname.anemone: ACTItemData(ItemClassification.useful, 1, "Stowaways"),
    iname.whelk: ACTItemData(ItemClassification.useful, 1, "Stowaways"),
    iname.rusty_nail: ACTItemData(ItemClassification.useful, 1, "Stowaways"),

    # currency
    iname.breadclaw: ACTItemData(ItemClassification.filler, 1, "Currency"),
    iname.chipclaw: ACTItemData(ItemClassification.filler, 1, "Currency"),
    iname.hairclaw: ACTItemData(ItemClassification.filler, 1, "Currency"),
    iname.clothesclaw: ACTItemData(ItemClassification.filler, 1, "Currency"),

    # consumable
    iname.barbed_hook: ACTItemData(ItemClassification.filler, 1, "Consumable"),

    # constume
    iname.captain_costume: ACTItemData(ItemClassification.filler, 1, "Costume")
}

item_name_to_id: Dict[str, int] = {name: item_base_id + index for index, name in enumerate(item_table)}

filler_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.filler]


def get_item_group(item_name: str) -> str:
    return item_table[item_name].item_group


item_name_groups: Dict[str, Set[str]] = {
    group: set(item_names) for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group) if group != ""
}