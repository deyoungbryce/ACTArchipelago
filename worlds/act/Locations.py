from typing import Dict, NamedTuple, Set, Optional
from itertools import groupby
from BaseClasses import Location
from .names import location_names as lname

location_base_id = 483021700

class ACTLocation(Location):
    game: str = "Another Crabs Treasure"

class ACTLocationData(NamedTuple):
    region: str
    location_id_offset: int
    location_group: Optional[str] = None


location_table: Dict[str, ACTLocationData] = {
    # starting item locations (will probably just include heartkelp_initial and fork pickup because they are the items you pick up right at the beginning of the game)
    #lname.heartkelp_inital: ACTLocationData("Tide Pools", "Starting Items"),
    lname.fork_pickup: ACTLocationData("Cave of Respite", 1, "Starting Items"),

    # progression item locations
    lname.fishing_line: ACTLocationData("Fort Slacktide", 2, "Fort Slacktide - Before Destruction"),
    lname.pristine_pearl: ACTLocationData("Moon Snail's Cave", 3, "Moon Snail's Cave"),
    
    # currency item locations
    lname.breadclaw_caveofrespite_ledge: ACTLocationData("Cave of Respite", 4, "Cave of Respite"),

    lname.breadclaw_shallows_southsandal: ACTLocationData("Central Shallows", 5, "Central Shallows Ground"),
    lname.breadclaw_shallows_westwall: ACTLocationData("Central Shallows", 6, "Central Shallows Ground"),
    lname.breadclaw_shallows_bridge: ACTLocationData("Central Shallows",  7, "Central Shallows Ground"),
    lname.breadclaw_shallows_eastwall: ACTLocationData("Central Shallows", 8, "Central Shallows Ground"),
    lname.breadclaw_shallows_eastsandal: ACTLocationData("Central Shallows", 9, "Central Shallows Ground"),
    lname.breadclaw_shallows_cigarette: ACTLocationData("Central Shallows", 10, "Central Shallows Ground"),
    lname.breadclaw_shallows_fortwall: ACTLocationData("Central Shallows", 11, "Central Shallows Ground"),
    lname.breadclaw_shallows_wallpiece: ACTLocationData("Central Shallows", 12, "Central Shallows Ground"),
    lname.breadclaw_shallows_sandcastle: ACTLocationData("Central Shallows", 13, "Central Shallows Grapple"),
    lname.breadclaw_shallows_eastledge: ACTLocationData("Central Shallows", 14, "Central Shallows Grapple"),
    lname.hairclaw_shallows_turret: ACTLocationData("Central Shallows", 15, "Central Shallows Grapple"),
    lname.chipclaw_shallows_sandcastle: ACTLocationData("Central Shallows", 16, "Central Shallows Grapple"),
    lname.clothesclaw_shallows_shellsplitter: ACTLocationData("Central Shallows", 17, "Central Shallows Grapple"),

    lname.breadclaw_slacktide_crates: ACTLocationData("Fort Slacktide", 18, "Fort Slacktide - Before Destruction"),

    lname.breadclaw_snailcave_entrance: ACTLocationData("Moon Snail's Cave", 19, "Moon Snail's Cave"),
    lname.breadclaw_snailcave_shortcut: ACTLocationData("Moon Snail's Cave", 20, "Moon Snail's Cave"),
    lname.breadclaw_snailcave_jelly: ACTLocationData("Moon Snail's Cave", 21, "Moon Snail's Cave"),

    lname.breadclaw_slacktide_crabtrio: ACTLocationData("Fort Slacktide", 22, "Fort Slacktide - After Destruction"),
    lname.chipclaw_slacktide_brokenwall: ACTLocationData("Fort Slacktide", 23, "Fort Slacktide - After Destruction"),

    # upgrade item locations
    lname.bloodstar_shallows_help: ACTLocationData("Central Shallows", 24, "Central Shallows Ground"),
    lname.bloodstar_shallows_parkour: ACTLocationData("Central Shallows", 25, "Central Shallows Ground"),
    lname.bloodstar_shallows_bridge: ACTLocationData("Central Shallows", 26, "Central Shallows Ground"),
    lname.bloodstar_shallows_clam: ACTLocationData("Central Shallows", 27, "Central Shallows Grapple"),

    lname.kelpsprout_snailcave_elevator: ACTLocationData("Moon Snail's Cave", 28, "Moon Snail's Cave"),
    lname.bloodstar_snailcave_platoon: ACTLocationData("Moon Snail's Cave", 29, "Moon Snail's Cave"),

    lname.bloodstar_slacktide_clam: ACTLocationData("Fort Slacktide", 30, "Fort Slacktide - After Destruction"),

    # stowaway locations
    lname.siphonophore_shallows_westwall: ACTLocationData("Central Shallows", 31, "Central Shallows Ground"),
    lname.seastar_shallows_eastledge: ACTLocationData("Central Shallows", 32, "Central Shallows Ground"),
    lname.whelk_shallows_dune: ACTLocationData("Central Shallows", 33, "Central Shallows Ground"),
    lname.sponge_shallows_puffer: ACTLocationData("Central Shallows", 34, "Central Shallows Grapple"),
    lname.anothercrab_shallows_pillar: ACTLocationData("Central Shallows", 35, "Central Shallows Grapple"),
    lname.sanddollar_shallows_arch: ACTLocationData("Central Shallows", 36, "Central Shallows Ground"),

    lname.limpet_slacktide_stairs: ACTLocationData("Fort Slacktide", 37, "Fort Slacktide - Before Destruction"),
    lname.seastar_slacktide_grappleroom: ACTLocationData("Fort Slacktide", 38, "Fort Slacktide - Before Destruction"),
    lname.barnacle_slacktide_bigurchin: ACTLocationData("Fort Slacktide", 39, "Fort Slacktide - Before Destruction"),

    lname.limpet_snailcave_jelly: ACTLocationData("Moon Snail's Cave", 40, "Moon Snail's Cave"),

    lname.mussel_slacktide_fortentrance: ACTLocationData("Fort Slacktide", 41, "Fort Slacktide - After Destruction"),
    lname.anemone_slacktide_fortwall: ACTLocationData("Fort Slacktide", 42, "Fort Slacktide - After Destruction"),
    lname.whelk_slacktide_turrettop: ACTLocationData("Fort Slacktide", 43, "Fort Slacktide - After Destruction"),

    # costume locations
    lname.captain_costume_pickup: ACTLocationData("Central Shallows", 44, "Central Shallows Ground"),

    # adaptation locations
    lname.royal_wave_reward: ACTLocationData("Fort Slacktide", 45, "Fort Slacktide - After Destruction")
}

#location_name_to_id: Dict[str, int] = {name: id for name, id in location_table.items()}
location_name_to_id: Dict[str, int] = {name: location_base_id + data.location_id_offset for name, data in location_table.items()}

location_name_groups: Dict[str, Set[str]] = {}
for loc_name, loc_data in location_table.items():
    if loc_data.location_group:
        location_name_groups.setdefault(loc_data.location_group, set()).add(loc_name)