from itertools import groupby
from typing import Dict, List, Set, NamedTuple
from BaseClasses import ItemClassification, Item
from .names import item_names as iname

class ACTItem(Item):
    game: str = "Another Crabs Treasure"

item_base_id = 483021700

class ACTItemData(NamedTuple):
    classification: ItemClassification
    quantity_in_item_pool: int
    item_id_offset: int
    item_group: str = ""

# a lot of quantities here will need to be adjusted later
item_table: Dict[str, ACTItemData] = {
    # progression
    #iname.fork: ACTItemData(ItemClassification.progression, 1, 1, "Progression"), 
    #iname.heartkelp_pod: ACTItemData(ItemClassification.progression, 1, 2, "Progression"), #throwing this into the progression items because the average player will definitely need heals to beat the game
    iname.fishing_line: ACTItemData(ItemClassification.progression, 1, 3, "Progression"),
    iname.pristine_pearl: ACTItemData(ItemClassification.progression, 1, 4, "Progression"),
    #iname.map_piece_fv: ACTItemData(ItemClassification.progression, 1, 5, "Progression"),
    #iname.map_piece_heikea: ACTItemData(ItemClassification.progression, 1, 6, "Progression"),
    #iname.map_piece_pagurus: ACTItemData(ItemClassification.progression, 1, 7, "Progression"),

    # upgrade
    iname.bloodstar_limb: ACTItemData(ItemClassification.useful, 6, 8, "Upgrades"), # total in game: 25
    iname.heartkelp_sprout: ACTItemData(ItemClassification.useful, 1, 9, "Upgrades"), # total in game: 7
    #iname.old_whorl: ACTItemData(ItemClassification.useful, 11, 10, "Upgrades"),
    #iname.stainless_relic: ACTItemData(ItemClassification.useful, 15, 11, "Upgrades"),
    #iname.tackle_pouch: ACTItemData(ItemClassification.useful, 1, 12, "Upgrades"),

    # stowaways
    iname.siphonophore: ACTItemData(ItemClassification.useful, 1, 13, "Stowaways"),
    iname.seastar: ACTItemData(ItemClassification.useful, 2, 14, "Stowaways"),
    iname.sponge: ACTItemData(ItemClassification.useful, 1, 15, "Stowaways"),
    iname.another_crab: ACTItemData(ItemClassification.useful, 1, 16, "Stowaways"),
    iname.sand_dollar: ACTItemData(ItemClassification.useful, 1, 17, "Stowaways"),
    iname.limpet: ACTItemData(ItemClassification.useful, 2, 18, "Stowaways"),
    iname.barnacle: ACTItemData(ItemClassification.useful, 1, 19, "Stowaways"),
    iname.mussel: ACTItemData(ItemClassification.useful, 1, 20, "Stowaways",),
    iname.anemone: ACTItemData(ItemClassification.useful, 1, 21, "Stowaways"),
    iname.whelk: ACTItemData(ItemClassification.useful, 2, 22, "Stowaways"),
    #iname.rusty_nail: ACTItemData(ItemClassification.useful, 1, 23, "Stowaways"),
    #iname.bobber: ACTItemData(ItemClassification.useful, 1, 24, "Stowaways"),
    #iname.chum: ACTItemData(ItemClassification.useful, 1, 25, "Stowaways"),
    #iname.cockle: ACTItemData(ItemClassification.useful, 1, 26, "Stowaways"),
    #iname.contact_lens: ACTItemData(ItemClassification.useful, 1, 27, "Stowaways"),
    #iname.cotton_ball: ACTItemData(ItemClassification.useful, 1, 28, "Stowaways"),
    #iname.fredrick: ACTItemData(ItemClassification.useful, 1, 29, "Stowaways"),
    #iname.fruit_sticker: ACTItemData(ItemClassification.useful, 1, 30, "Stowaways"),
    #iname.googly_eye: ACTItemData(ItemClassification.useful, 1, 31, "Stowaways"),
    #iname.lamprey: ACTItemData(ItemClassification.useful, 1, 32, "Stowaways"),
    #iname.lanternfish: ACTItemData(ItemClassification.useful, 1, 33, "Stowaways"),
    #iname.lumpsucker: ACTItemData(ItemClassification.useful, 1, 34, "Stowaways"),
    #iname.oyster: ACTItemData(ItemClassification.useful, 1, 35, "Stowaways"),
    #iname.packing_peanut: ACTItemData(ItemClassification.useful, 1, 36, "Stowaways"),
    #iname.phytoplankton: ACTItemData(ItemClassification.useful, 1, 37, "Stowaways"),
    #iname.puffer_quill: ACTItemData(ItemClassification.useful, 1, 38, "Stowaways"),
    #iname.rubber_band: ACTItemData(ItemClassification.useful, 1, 39, "Stowaways"),
    #iname.salp: ACTItemData(ItemClassification.useful, 1, 40, "Stowaways"),
    #iname.sea_cucumber: ACTItemData(ItemClassification.useful, 1, 41, "Stowaways"),
    #iname.shark_tooth: ACTItemData(ItemClassification.useful, 1, 42, "Stowaways"),
    #iname.sinker: ACTItemData(ItemClassification.useful, 1, 43, "Stowaways"),
    #iname.small_battery: ACTItemData(ItemClassification.useful, 1, 44, "Stowaways"),
    #iname.turtle_shell_shard: ACTItemData(ItemClassification.useful, 1, 45, "Stowaways"),
    #iname.used_bandage: ACTItemData(ItemClassification.useful, 1, 46, "Stowaways"),
    #iname.wad_of_gum: ACTItemData(ItemClassification.useful, 1, 47, "Stowaways"),
    #iname.zooplankton: ACTItemData(ItemClassification.useful, 1, 48, "Stowaways"),

    # currency
    iname.breadclaw: ACTItemData(ItemClassification.filler, 16, 49, "Currency"),
    iname.chipclaw: ACTItemData(ItemClassification.filler, 2, 50, "Currency"),
    iname.hairclaw: ACTItemData(ItemClassification.filler, 1, 51, "Currency"),
    iname.clothesclaw: ACTItemData(ItemClassification.filler, 1, 52, "Currency"),
    #iname.paperclaw: ACTItemData(ItemClassification.filler, 1, 53, "Currency"),
    #iname.stapleclaw: ACTItemData(ItemClassification.filler, 1, 54, "Currency"),
    #iname.carclaw: ACTItemData(ItemClassification.filler, 1, 55, "Currency"),

    # consumable
    #iname.barbed_hook: ACTItemData(ItemClassification.filler, 1, 56, "Consumable"),

    # constume
    #iname.plastic_poncho: ACTItemData(ItemClassification.filler, 1, 57, "Costume"),
    iname.captain_costume: ACTItemData(ItemClassification.filler, 1, 58, "Costume"),
    #iname.dr_kril: ACTItemData(ItemClassification.filler, 1, 59, "Costume"),
    #iname.exiled_flame: ACTItemData(ItemClassification.filler, 1, 60, "Costume"),
    #iname.blackout_poncho: ACTItemData(ItemClassification.filler, 1, 61, "Costume"),
    #iname.ivory_poncho: ACTItemData(ItemClassification.filler, 1, 62, "Costume"),
    #iname.intern: ACTItemData(ItemClassification.filler, 1, 63, "Costume"),
    #iname.sunlight: ACTItemData(ItemClassification.filler, 1, 64, "Costume"),
    #iname.krillionaire: ACTItemData(ItemClassification.filler, 1, 65, "Costume"),
    #iname.midnight: ACTItemData(ItemClassification.filler, 1, 66, "Costume"),
    #iname.maid_kril: ACTItemData(ItemClassification.filler, 1, 67, "Costume"),
    #iname.rainbow_crabitalism: ACTItemData(ItemClassification.filler, 1, 68, "Costume"),
    #iname.mr_kril: ACTItemData(ItemClassification.filler, 1, 69, "Costume"),
    #iname.cowfishboy: ACTItemData(ItemClassification.filler, 1, 70, "Costume"),
    #iname.cult_leader: ACTItemData(ItemClassification.filler, 1, 71, "Costume"),
    #iname.blue_collar: ACTItemData(ItemClassification.filler, 1, 72, "Costume"),

}

#item_name_to_id: Dict[str, int] = {name: id for name, id in item_table.items()}
item_name_to_id: Dict[str, int] = {name: item_base_id + data.item_id_offset for name, data in item_table.items()}

filler_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.filler]


def get_item_group(item_name: str) -> str:
    return item_table[item_name].item_group


item_name_groups: Dict[str, Set[str]] = {
    group: set(item_names) for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group) if group != ""
}