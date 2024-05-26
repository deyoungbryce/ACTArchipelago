from itertools import groupby
from typing import Dict, List, Set, NamedTuple
from BaseClasses import ItemClassification
from .names import item_names as iname

item_base_id = 483021700

class ACTItemData(NamedTuple):
    classification: ItemClassification
    quantity_in_item_pool: int
    item_group: str = ""
    id: int

# a lot of quantities here will need to be adjusted later
item_table: Dict[str, ACTItemData] = {
    # progression
    iname.fork: ACTItemData(ItemClassification.progression, 1, "Progression", item_base_id+1), 
    iname.heartkelp_pod: ACTItemData(ItemClassification.progression, 1, "Progression", item_base_id+2), #throwing this into the progression items because the average player will definitely need heals to beat the game
    iname.fishing_line: ACTItemData(ItemClassification.progression, 1, "Progression", item_base_id+3),
    iname.pristine_pearl: ACTItemData(ItemClassification.progression, 1, "Progression", item_base_id+4),
    iname.map_piece_fv: ACTItemData(ItemClassification.progression, 1, "Progression", item_base_id+5),
    iname.map_piece_heikea: ACTItemData(ItemClassification.progression, 1, "Progression", item_base_id+6),
    iname.map_piece_pagurus: ACTItemData(ItemClassification.progression, 1, "Progression", item_base_id+7),

    # upgrade
    iname.bloodstar_limb: ACTItemData(ItemClassification.useful, 25 , "Upgrades", item_base_id+8),
    iname.heartkelp_sprout: ACTItemData(ItemClassification.useful, 7, "Upgrades", item_base_id+9),
    iname.old_whorl: ACTItemData(ItemClassification.useful, 11, "Upgrades", item_base_id+10),
    iname.stainless_relic: ACTItemData(ItemClassification.useful, 15, "Upgrades", item_base_id+11),
    iname.tackle_pouch: ACTItemData(ItemClassification.useful, 1, "Upgrades", item_base_id+12),

    # stowaways
    iname.siphonophore: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+13),
    iname.seastar: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+14),
    iname.sponge: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+15),
    iname.another_crab: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+16),
    iname.sand_dollar: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+17),
    iname.limpet: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+18),
    iname.barnacle: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+19),
    iname.mussel: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+20),
    iname.anemone: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+21),
    iname.whelk: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+22),
    iname.rusty_nail: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+23),
    iname.bobber: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+24),
    iname.chum: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+25),
    iname.cockle: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+26),
    iname.contact_lens: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+27),
    iname.cotton_ball: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+28),
    iname.fredrick: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+29),
    iname.fruit_sticker: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+30),
    iname.googly_eye: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+31),
    iname.lamprey: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+32),
    iname.lanternfish: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+33),
    iname.lumpsucker: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+34),
    iname.oyster: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+35),
    iname.packing_peanut: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+36),
    iname.phytoplankton: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+37),
    iname.puffer_quill: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+38),
    iname.rubber_band: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+39),
    iname.salp: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+40),
    iname.sea_cucumber: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+41),
    iname.shark_tooth: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+42),
    iname.sinker: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+43),
    iname.small_battery: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+44),
    iname.turtle_shell_shard: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+45),
    iname.used_bandage: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+46),
    iname.wad_of_gum: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+47),
    iname.zooplankton: ACTItemData(ItemClassification.useful, 1, "Stowaways", item_base_id+48),

    # currency
    iname.breadclaw: ACTItemData(ItemClassification.filler, 1, "Currency", item_base_id+49),
    iname.chipclaw: ACTItemData(ItemClassification.filler, 1, "Currency", item_base_id+50),
    iname.hairclaw: ACTItemData(ItemClassification.filler, 1, "Currency", item_base_id+51),
    iname.clothesclaw: ACTItemData(ItemClassification.filler, 1, "Currency", item_base_id+52),
    iname.paperclaw: ACTItemData(ItemClassification.filler, 1, "Currency", item_base_id+53),
    iname.stapleclaw: ACTItemData(ItemClassification.filler, 1, "Currency", item_base_id+54),
    iname.carclaw: ACTItemData(ItemClassification.filler, 1, "Currency", item_base_id+55),

    # consumable
    iname.barbed_hook: ACTItemData(ItemClassification.filler, 1, "Consumable", item_base_id+56),

    # constume
    iname.plastic_poncho: ACTItemData(ItemClassification.filler, 1, "Costume", item_base_id+57),
    iname.captain_costume: ACTItemData(ItemClassification.filler, 1, "Costume", item_base_id+58),
    iname.dr_kril: ACTItemData(ItemClassification.filler, 1, "Costume", item_base_id+59),
    iname.exiled_flame: ACTItemData(ItemClassification.filler, 1, "Costume", item_base_id+60),
    iname.blackout_poncho: ACTItemData(ItemClassification.filler, 1, "Costume", item_base_id+61),
    iname.ivory_poncho: ACTItemData(ItemClassification.filler, 1, "Costume", item_base_id+62),
    iname.intern: ACTItemData(ItemClassification.filler, 1, "Costume", item_base_id+63),
    iname.sunlight: ACTItemData(ItemClassification.filler, 1, "Costume", item_base_id+64),
    iname.krillionaire: ACTItemData(ItemClassification.filler, 1, "Costume", item_base_id+65),
    iname.midnight: ACTItemData(ItemClassification.filler, 1, "Costume", item_base_id+66),
    iname.maid_kril: ACTItemData(ItemClassification.filler, 1, "Costume", item_base_id+67),
    iname.rainbow_crabitalism: ACTItemData(ItemClassification.filler, 1, "Costume", item_base_id+68),
    iname.mr_kril: ACTItemData(ItemClassification.filler, 1, "Costume", item_base_id+69),
    iname.cowfishboy: ACTItemData(ItemClassification.filler, 1, "Costume", item_base_id+70),
    iname.cult_leader: ACTItemData(ItemClassification.filler, 1, "Costume", item_base_id+71),
    iname.blue_collar: ACTItemData(ItemClassification.filler, 1, "Costume", item_base_id+72),

}

#item_name_to_id: Dict[str, int] = {name: item_base_id + index for index, name in enumerate(item_table)}

def get_item_id(item_name: str) -> int:
    return item_table[item_name].id

item_ids: Dict[str, Set[int]] = {
    id: set(item_id) for id, item_id in groupby(sorted(item_table, key=get_item_id), get_item_id) if id != None
}

filler_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.filler]


def get_item_group(item_name: str) -> str:
    return item_table[item_name].item_group


item_name_groups: Dict[str, Set[str]] = {
    group: set(item_names) for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group) if group != ""
}