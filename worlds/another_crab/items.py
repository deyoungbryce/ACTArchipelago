from itertools import groupby
from typing import Dict, List, Set, NamedTuple
from BaseClasses import ItemClassification, Item

from .names import item_names as iname

class ACTItem(Item):
    game: str = "Another Crabs Treasure"

item_base_id: int = 483021700

class ACTItemData(NamedTuple):
    classification: ItemClassification
    quantity_in_item_pool: int
    item_id_offset: int
    item_group: str = ""


# a lot of quantities here will need to be adjusted later
item_table: Dict[str, ACTItemData] = {
    # progression
    iname.fork: ACTItemData(ItemClassification.progression, 1, 1, "Progression"), 
    #iname.heartkelp_pod: ACTItemData(ItemClassification.progression, 1, 2, "Progression"), #throwing this into the progression items because the average player will definitely need heals to beat the game.
    iname.fishing_line: ACTItemData(ItemClassification.progression, 1, 3, "Progression"),
    iname.pristine_pearl: ACTItemData(ItemClassification.progression, 1, 4, "Progression"),
    iname.map_piece_fv: ACTItemData(ItemClassification.progression, 1, 5, "Progression"),
    iname.map_piece_heikea: ACTItemData(ItemClassification.progression, 1, 6, "Progression"), 
    iname.map_piece_pagurus: ACTItemData(ItemClassification.progression, 1, 7, "Progression"), 

    # upgrade
    iname.bloodstar_limb: ACTItemData(ItemClassification.useful, 20, 8, "Upgrades"), # total in game: 25
    iname.heartkelp_sprout: ACTItemData(ItemClassification.useful, 7, 9, "Upgrades"), # total in game: 7
    iname.old_whorl: ACTItemData(ItemClassification.useful, 11, 10, "Upgrades"),
    iname.stainless_relic: ACTItemData(ItemClassification.useful, 16, 11, "Upgrades"),
    iname.tackle_pouch: ACTItemData(ItemClassification.useful, 5, 12, "Upgrades"),

    # stowaways
    iname.anemone: ACTItemData(ItemClassification.useful, 10, 13, "Stowaways"),
    iname.anemone_plus: ACTItemData(ItemClassification.useful, 4, 14, "Stowaways"),
    iname.anemone_plus_plus: ACTItemData(ItemClassification.useful, 1, 15, "Stowaways"),
    iname.another_crab: ACTItemData(ItemClassification.useful, 7, 16, "Stowaways"),
    iname.barnacle: ACTItemData(ItemClassification.useful, 7, 17, "Stowaways"),
    iname.barnacle_plus: ACTItemData(ItemClassification.useful, 2, 18, "Stowaways"),
    iname.barnacle_plusplus: ACTItemData(ItemClassification.useful, 1, 19, "Stowaways"),
    #iname.bleached_phytoplankton: ACTItemData(ItemClassification.useful, 1, 20, "Stowaways"), #Not used in base game
    iname.bobber: ACTItemData(ItemClassification.useful, 1, 21, "Stowaways"),
    iname.chum: ACTItemData(ItemClassification.useful, 1, 22, "Stowaways"),
    iname.cockle: ACTItemData(ItemClassification.useful, 3, 23, "Stowaways"),
    iname.cockle_plus: ACTItemData(ItemClassification.useful, 1, 113, "Stowaways"), #missed on first pass oops
    iname.contact_lens: ACTItemData(ItemClassification.useful, 1, 24, "Stowaways"),
    iname.cotton_ball: ACTItemData(ItemClassification.useful, 1, 25, "Stowaways"),
    iname.earthworm: ACTItemData(ItemClassification.useful, 1, 114, "Stowaways"), #missed on first pass oops
    iname.fredrick: ACTItemData(ItemClassification.useful, 1, 26, "Stowaways"),
    iname.fruit_sticker: ACTItemData(ItemClassification.useful, 2, 27, "Stowaways"),
    iname.fruit_sticker_plus: ACTItemData(ItemClassification.useful, 1, 28, "Stowaways"),
    iname.googly_eye: ACTItemData(ItemClassification.useful, 3, 29, "Stowaways"),
    iname.lamprey: ACTItemData(ItemClassification.useful, 1, 30, "Stowaways"),
    iname.lamprey_plus: ACTItemData(ItemClassification.useful, 1, 31, "Stowaways"),
    iname.lanternfish: ACTItemData(ItemClassification.useful, 1, 32, "Stowaways"),
    iname.limpet: ACTItemData(ItemClassification.useful, 12, 33, "Stowaways"),
    iname.limpet_plus: ACTItemData(ItemClassification.useful, 2, 34, "Stowaways"),
    iname.limpet_plus_plus: ACTItemData(ItemClassification.useful, 2, 35, "Stowaways"),
    iname.lugnut: ACTItemData(ItemClassification.useful, 1, 36, "Stowaways"),
    iname.lumpsucker: ACTItemData(ItemClassification.useful, 3, 37, "Stowaways"),
    iname.lumpsucker_plus: ACTItemData(ItemClassification.useful, 1, 38, "Stowaways"),
    iname.mussel: ACTItemData(ItemClassification.useful, 10, 39, "Stowaways",),
    iname.mussel_plus: ACTItemData(ItemClassification.useful, 5, 40, "Stowaways",),
    iname.mussel_plus_plus: ACTItemData(ItemClassification.useful, 1, 41, "Stowaways",),
    iname.oyster: ACTItemData(ItemClassification.useful, 3, 42, "Stowaways"),
    iname.packing_peanut: ACTItemData(ItemClassification.useful, 1, 43, "Stowaways"),
    iname.phytoplankton: ACTItemData(ItemClassification.useful, 1, 44, "Stowaways"),
    iname.phytoplankton_plus: ACTItemData(ItemClassification.useful, 2, 45, "Stowaways"),
    iname.puffer_quill: ACTItemData(ItemClassification.useful, 3, 46, "Stowaways"),
    iname.razor_blade: ACTItemData(ItemClassification.useful, 1, 47, "Stowaways"),
    iname.rubber_band: ACTItemData(ItemClassification.useful, 1, 48, "Stowaways"),
    iname.rusty_nail: ACTItemData(ItemClassification.useful, 6, 49, "Stowaways"),
    iname.rusty_nail_plus: ACTItemData(ItemClassification.useful, 3, 50, "Stowaways"),
    iname.salp: ACTItemData(ItemClassification.useful, 3, 51, "Stowaways"),
    iname.salp_plus: ACTItemData(ItemClassification.useful, 2, 52, "Stowaways"),
    iname.sand_dollar: ACTItemData(ItemClassification.useful, 9, 53, "Stowaways"),
    iname.sea_cucumber: ACTItemData(ItemClassification.useful, 2, 54, "Stowaways"),
    iname.seaslug: ACTItemData(ItemClassification.useful, 1, 55, "Stowaways"),
    iname.seastar: ACTItemData(ItemClassification.useful, 7, 56, "Stowaways"),
    iname.seastar_plus: ACTItemData(ItemClassification.useful, 4, 57, "Stowaways"),
    iname.seastar_plus_plus: ACTItemData(ItemClassification.useful, 2, 58, "Stowaways"),
    iname.shark_tooth: ACTItemData(ItemClassification.useful, 1, 59, "Stowaways"),
    iname.shark_tooth_plus: ACTItemData(ItemClassification.useful, 1, 60, "Stowaways"),
    iname.sinker: ACTItemData(ItemClassification.useful, 2, 61, "Stowaways"),
    iname.sinker_plus: ACTItemData(ItemClassification.useful, 3, 62, "Stowaways"),
    iname.sinker_plus_plus: ACTItemData(ItemClassification.useful, 1, 63, "Stowaways"),
    iname.siphonophore: ACTItemData(ItemClassification.useful, 2, 64, "Stowaways"),
    iname.siphonophore_plus: ACTItemData(ItemClassification.useful, 3, 65, "Stowaways"),
    iname.small_battery: ACTItemData(ItemClassification.useful, 1, 66, "Stowaways"),
    iname.small_battery_plus: ACTItemData(ItemClassification.useful, 1, 67, "Stowaways"),
    iname.sponge: ACTItemData(ItemClassification.useful, 3, 68, "Stowaways"),
    iname.sponge_plus: ACTItemData(ItemClassification.useful, 1, 69, "Stowaways"),
    iname.turtle_shell_shard: ACTItemData(ItemClassification.useful, 2, 70, "Stowaways"),
    #iname.ur: ACTItemData(ItemClassification.useful, 1, 71, "Stowaways"), #Not used in base game
    iname.used_bandage: ACTItemData(ItemClassification.useful, 1, 72, "Stowaways"),
    iname.used_bandage_plus: ACTItemData(ItemClassification.useful, 1, 73, "Stowaways"),
    iname.wad_of_gum: ACTItemData(ItemClassification.useful, 1, 74, "Stowaways"),
    iname.whelk: ACTItemData(ItemClassification.useful, 3, 75, "Stowaways"),
    iname.whelk_plus: ACTItemData(ItemClassification.useful, 2, 76, "Stowaways"),
    iname.whelk_plus_plus: ACTItemData(ItemClassification.useful, 2, 77, "Stowaways"),
    iname.zooplankton: ACTItemData(ItemClassification.useful, 1, 78, "Stowaways"),
    iname.zooplankton_plus: ACTItemData(ItemClassification.useful, 1, 79, "Stowaways"),

    # currency
    iname.breadclaw: ACTItemData(ItemClassification.filler, 55, 80, "Currency"),
    iname.chipclaw: ACTItemData(ItemClassification.filler, 35, 81, "Currency"),
    iname.hairclaw: ACTItemData(ItemClassification.filler, 49, 82, "Currency"),
    iname.clothesclaw: ACTItemData(ItemClassification.filler, 48, 83, "Currency"),
    iname.paperclaw: ACTItemData(ItemClassification.filler, 29, 84, "Currency"),
    iname.stapleclaw: ACTItemData(ItemClassification.filler, 10, 85, "Currency"),
    iname.carclaw: ACTItemData(ItemClassification.filler, 8, 86, "Currency"),

    # consumable
    iname.barbed_hook: ACTItemData(ItemClassification.filler, 116, 87, "Consumable"),
    iname.shark_egg: ACTItemData(ItemClassification.filler, 4, 133, "Consumable"),

    # costume
    iname.plastic_poncho: ACTItemData(ItemClassification.filler, 1, 88, "Costume"),
    iname.captain_costume: ACTItemData(ItemClassification.filler, 1, 89, "Costume"),
    iname.dr_kril: ACTItemData(ItemClassification.filler, 1, 90, "Costume"),
    iname.exiled_flame: ACTItemData(ItemClassification.filler, 1, 91, "Costume"),
    iname.blackout_poncho: ACTItemData(ItemClassification.filler, 1, 92, "Costume"),
    iname.ivory_poncho: ACTItemData(ItemClassification.filler, 1, 93, "Costume"),
    iname.intern: ACTItemData(ItemClassification.filler, 1, 94, "Costume"),
    iname.sunlight: ACTItemData(ItemClassification.filler, 1, 95, "Costume"),
    iname.krillionaire: ACTItemData(ItemClassification.filler, 1, 96, "Costume"),
    iname.midnight: ACTItemData(ItemClassification.filler, 1, 97, "Costume"),
    iname.maid_kril: ACTItemData(ItemClassification.filler, 1, 98, "Costume"),
    iname.rainbow_crabitalism: ACTItemData(ItemClassification.filler, 1, 99, "Costume"),
    iname.mr_kril: ACTItemData(ItemClassification.filler, 1, 100, "Costume"),
    iname.cowfishboy: ACTItemData(ItemClassification.filler, 1, 101, "Costume"),
    iname.cult_leader: ACTItemData(ItemClassification.filler, 1, 102, "Costume"),
    iname.blue_collar: ACTItemData(ItemClassification.filler, 1, 103, "Costume"),
    iname.clown: ACTItemData(ItemClassification.filler, 1, 104, "Costume"),

    # adaptations
    iname.royal_wave: ACTItemData(ItemClassification.useful, 1, 105, "Adapations"),
    iname.bobbit_trap: ACTItemData(ItemClassification.useful, 1, 106, "Adapations"),
    iname.bubble_bullet: ACTItemData(ItemClassification.useful, 1, 107, "Adapations"),
    iname.eelectrocute: ACTItemData(ItemClassification.progression, 1, 108, "Adapations"),
    iname.mantis_punch: ACTItemData(ItemClassification.useful, 1, 109, "Adapations"),
    iname.snail_sanctum: ACTItemData(ItemClassification.useful, 1, 110, "Adapations"),
    iname.spectral_tentacle: ACTItemData(ItemClassification.useful, 1, 111, "Adapations"),
    iname.urchin_toss: ACTItemData(ItemClassification.useful, 1, 112, "Adapations"),

    iname.shelleport: ACTItemData(ItemClassification.progression, 1, 133, "Skills"),
    iname.skeddadle: ACTItemData(ItemClassification.useful, 1, 134, "Skills"),
    iname.parry: ACTItemData(ItemClassification.useful, 1, 113, "Skills"),
    iname.riposte: ACTItemData(ItemClassification.useful, 1, 114, "Skills"),
    iname.natural_defenses: ACTItemData(ItemClassification.useful, 1, 115, "Skills"),
    iname.aggravation: ACTItemData(ItemClassification.useful, 1, 116, "Skills"),
    iname.self_repair: ACTItemData(ItemClassification.useful, 1, 117, "Skills"),
    iname.kintsugi: ACTItemData(ItemClassification.useful, 1, 118, "Skills"),
    iname.skewer: ACTItemData(ItemClassification.useful, 1, 119, "Skills"),
    iname.plunge: ACTItemData(ItemClassification.useful, 1, 120, "Skills"),
    iname.scrap_hammer: ACTItemData(ItemClassification.useful, 1, 121, "Skills"),
    iname.dispatch: ACTItemData(ItemClassification.useful, 1, 122, "Skills"),
    iname.spearfishing: ACTItemData(ItemClassification.useful, 1, 123, "Skills"),
    iname.wave_breaker: ACTItemData(ItemClassification.useful, 1, 124, "Skills"),
    iname.streamline: ACTItemData(ItemClassification.useful, 1, 125, "Skills"),
    iname.housewarming: ACTItemData(ItemClassification.useful, 1, 126, "Skills"),
    iname.circle_of_life: ACTItemData(ItemClassification.useful, 1, 127, "Skills"),
    iname.elusive_prey: ACTItemData(ItemClassification.useful, 1, 128, "Skills"),
    iname.ebb_and_flow: ACTItemData(ItemClassification.useful, 1, 129, "Skills"),
    iname.umami_training1: ACTItemData(ItemClassification.useful, 1, 130, "Skills"),
    iname.umami_training2: ACTItemData(ItemClassification.useful, 1, 131, "Skills"),
    iname.umami_training3: ACTItemData(ItemClassification.useful, 1, 132, "Skills"),

    # traps
    #iname.trap_example: ACTItemData(ItemClassification.trap, ~, ~, "Traps")

}

item_name_to_id: Dict[str, int] = {name: item_base_id + data.item_id_offset for name, data in item_table.items()}

def get_item_group(item_name: str) -> str:
    return item_table[item_name].item_group

filler_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.filler and get_item_group != "Costume"]

costume_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.filler and get_item_group == "Costume"]

item_name_groups: Dict[str, Set[str]] = {
    group: set(item_names) for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group) if group != ""
}