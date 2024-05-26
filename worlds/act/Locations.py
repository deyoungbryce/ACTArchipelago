from typing import Dict, NamedTuple, Set, Optional
from itertools import groupby
from .names import location_names as lname

location_base_id = 483021700

class ACTLocationData(NamedTuple):
    region: str
    location_group: Optional[str] = None
    id: int


location_table: Dict[str, ACTLocationData] = {
    # starting item locations (will probably just include heartkelp_initial and fork pickup because they are the items you pick up right at the beginning of the game)
    #lname.heartkelp_inital: ACTLocationData("Tide Pools", "Starting Items"),
    lname.fork_pickup: ACTLocationData("Cave of Respite", "Starting Items", location_base_id+1),

    # progression item locations
    lname.fishing_line: ACTLocationData("Fort Slacktide", "Fort Slacktide - Before Destruction", location_base_id+2),
    lname.pristine_pearl: ACTLocationData("Moon Snail's Cave", "Moon Snail's Cave", location_base_id+3),
    
    # currency item locations
    lname.breadclaw_caveofrespite_ledge: ACTLocationData("Cave of Respite", "Cave of Respite", location_base_id+4),

    lname.breadclaw_shallows_southsandal: ACTLocationData("Central Shallows", "Central Shallows Ground", location_base_id+5),
    lname.breadclaw_shallows_westwall: ACTLocationData("Central Shallows", "Central Shallows Ground", location_base_id+6),
    lname.breadclaw_shallows_bridge: ACTLocationData("Central Shallows", "Central Shallows Ground", location_base_id+7),
    lname.breadclaw_shallows_eastwall: ACTLocationData("Central Shallows", "Central Shallows Ground", location_base_id+8),
    lname.breadclaw_shallows_eastsandal: ACTLocationData("Central Shallows", "Central Shallows Ground", location_base_id+9),
    lname.breadclaw_shallows_cigarette: ACTLocationData("Central Shallows", "Central Shallows Ground", location_base_id+10),
    lname.breadclaw_shallows_fortwall: ACTLocationData("Central Shallows", "Central Shallows Ground", location_base_id+11),
    lname.breadclaw_shallows_wallpiece: ACTLocationData("Central Shallows", "Central Shallows Ground", location_base_id+12),
    lname.breadclaw_shallows_sandcastle: ACTLocationData("Central Shallows", "Central Shallows Grapple", location_base_id+13),
    lname.breadclaw_shallows_eastledge: ACTLocationData("Central Shallows", "Central Shallows Grapple", location_base_id+14),
    lname.hairclaw_shallows_turret: ACTLocationData("Central Shallows", "Central Shallows Grapple", location_base_id+15),
    lname.chipclaw_shallows_sandcastle: ACTLocationData("Central Shallows", "Central Shallows Grapple", location_base_id+16),
    lname.clothesclaw_shallows_shellsplitter: ACTLocationData("Central Shallows", "Central Shallows Grapple", location_base_id+17),

    lname.breadclaw_slacktide_crates: ACTLocationData("Fort Slacktide", "Fort Slacktide - Before Destruction", location_base_id+18),

    lname.breadclaw_snailcave_entrance: ACTLocationData("Moon Snail's Cave", "Moon Snail's Cave", location_base_id+19),
    lname.breadclaw_snailcave_shortcut: ACTLocationData("Moon Snail's Cave", "Moon Snail's Cave", location_base_id+20),
    lname.breadclaw_snailcave_jelly: ACTLocationData("Moon Snail's Cave", "Moon Snail's Cave", location_base_id+21),

    lname.breadclaw_slacktide_crabtrio: ACTLocationData("Fort Slacktide", "Fort Slacktide - After Destruction", location_base_id+22),
    lname.chipclaw_slacktide_brokenwall: ACTLocationData("Fort Slacktide", "Fort Slacktide - After Destruction", location_base_id+23),

    # upgrade item locations
    lname.bloodstar_shallows_help: ACTLocationData("Central Shallows", "Central Shallows Ground", location_base_id+24),
    lname.bloodstar_shallows_parkour: ACTLocationData("Central Shallows", "Central Shallows Ground", location_base_id+25),
    lname.bloodstar_shallows_bridge: ACTLocationData("Central Shallows", "Central Shallows Ground", location_base_id+26),
    lname.bloodstar_shallows_clam: ACTLocationData("Central Shallows", "Central Shallows Grapple", location_base_id+27),

    lname.kelpsprout_snailcave_elevator: ACTLocationData("Moon Snail's Cave", "Moon Snail's Cave", location_base_id+28),
    lname.bloodstar_snailcave_platoon: ACTLocationData("Moon Snail's Cave", "Moon Snail's Cave", location_base_id+29),

    lname.bloodstar_slacktide_clam: ACTLocationData("Fort Slacktide", "Fort Slacktide - After Destruction", location_base_id+30),

    # stowaway locations
    lname.siphonophore_shallows_westwall: ACTLocationData("Central Shallows", "Central Shallows Ground", location_base_id+31),
    lname.seastar_shallows_eastledge: ACTLocationData("Central Shallows", "Central Shallows Ground", location_base_id+32),
    lname.whelk_shallows_dune: ACTLocationData("Central Shallows", "Central Shallows Ground", location_base_id+33),
    lname.sponge_shallows_puffer: ACTLocationData("Central Shallows", "Central Shallows Grapple"),
    lname.anothercrab_shallows_pillar: ACTLocationData("Central Shallows", "Central Shallows Grapple", location_base_id+34),
    lname.sanddollar_shallows_arch: ACTLocationData("Central Shallows", "Central Shallows Ground", location_base_id+35),

    lname.limpet_slacktide_stairs: ACTLocationData("Fort Slacktide", "Fort Slacktide - Before Destruction", location_base_id+36),
    lname.seastar_slacktide_grappleroom: ACTLocationData("Fort Slacktide", "Fort Slacktide - Before Destruction", location_base_id+37),
    lname.barnacle_slacktide_bigurchin: ACTLocationData("Fort Slacktide", "Fort Slacktide - Before Destruction", location_base_id+38),

    lname.limpet_snailcave_jelly: ACTLocationData("Moon Snail's Cave", "Moon Snail's Cave", location_base_id+39),

    lname.mussel_slacktide_fortentrance: ACTLocationData("Fort Slacktide", "Fort Slacktide - After Destruction", location_base_id+40),
    lname.anemone_slacktide_fortwall: ACTLocationData("Fort Slacktide", "Fort Slacktide - After Destruction", location_base_id+41),
    lname.whelk_slacktide_turrettop: ACTLocationData("Fort Slacktide", "Fort Slacktide - After Destruction", location_base_id+42),

    # costume locations
    lname.captain_costume_pickup: ACTLocationData("Central Shallows", "Central Shallows Ground", location_base_id+43),

    # adaptation locations
    lname.royal_wave_reward: ACTLocationData("Fort Slacktide", "Fort Slacktide - After Destruction", location_base_id+44)
}

#location_name_to_id: Dict[str, int] = {name: location_base_id + index for index, name in enumerate(location_table)}

def get_location_id(location_name: str) -> int:
    return location_table[location_name].id

location_ids: Dict[str, Set[int]] = {
    id: set(location_id) for id, location_id in groupby(sorted(location_table, key=get_location_id), get_location_id) if id != None
}

location_name_groups: Dict[str, Set[str]] = {}
for loc_name, loc_data in location_table.items():
    if loc_data.location_group:
        location_name_groups.setdefault(loc_data.location_group, set()).add(loc_name)